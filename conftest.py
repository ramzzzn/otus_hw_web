import logging
import datetime
import os
import random

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options as ChromiumOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.service import Service as SafariService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--remote", action="store_true", default=True)
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--base_url", action="store", default="http://172.22.144.70:8081")
    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption("--ya_driver", default="C:/otus_homeworks/homework_web/drivers/yandexdriver.exe")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--brws_vers", default="124.0")
    parser.addoption("--video", action="store_true", default=False)
    parser.addoption("--vnc", action="store_true", default=True)


def setup_logger(name: str, log_level: str) -> logging.Logger:
    # создаем папку logs, если её нет
    if not os.path.exists("logs"):
        os.makedirs("logs")
    logger = logging.getLogger(name)
    # задаем путь, где будут храниться логи
    file_handler = logging.FileHandler(f"logs/{name}.log")
    # задаем формат логов
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    return logger


def local_execute(browser_name, headless, ya_driver):
    # настраиваем веб-драйвер, согласно выбранному браузеру:
    if browser_name == "chrome":
        service = ChromiumService()
        options = ChromiumOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        service = FirefoxService()
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(service=service, options=options)
    elif browser_name == "edge":
        service = EdgeService()
        options = EdgeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Edge(service=service, options=options)
    elif browser_name == "yandex":
        service = ChromiumService(executable_path=ya_driver)
        options = ChromiumOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "safari":
        service = SafariService()
        driver = webdriver.Safari(service=service)

    return driver


def remote_execute(executor, browser_name, version, vnc, video):
    executor_url = f"http://{executor}:4444/wd/hub"
    # настраиваем веб-драйвер, согласно выбранному браузеру:
    if browser_name == "chrome":
        options = ChromiumOptions()
    elif browser_name == "firefox":
        options = FirefoxOptions()
    elif browser_name == "edge":
        options = EdgeOptions()

    caps = {
        "browserName": browser_name,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "name": os.getenv("Homework_№8", str(random.randint(9000, 10000))),
            "enableVideo": video,
            "timeZone": "Europe/Moscow",
            "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"],
            "sessionTimeout": "1m"

        },
        "acceptInsecureCerts": True,
    }

    for k, v in caps.items():
        options.set_capability(k, v)

    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )

    return driver


@pytest.fixture
def browser(request):
    # присваиваем полученные значения при запуске
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--base_url")
    headless = request.config.getoption("--headless")
    ya_driver = request.config.getoption("--ya_driver")
    log_level = request.config.getoption("--log_level")
    remote = request.config.getoption("--remote")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--brws_vers")
    video = request.config.getoption("--video")
    vnc = request.config.getoption("--video")

    # настраиваем логирование
    logger = setup_logger(request.node.name, log_level)
    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    # если запуск тестов выполняется удаленно
    if remote:
        _browser = remote_execute(executor, browser_name, version, vnc, video)
    # если запуск тестов выполняется локально
    else:
        _browser = local_execute(browser_name, headless, ya_driver)

    _browser.maximize_window()
    _browser.log_level = log_level
    _browser.logger = logger
    _browser.test_name = request.node.name
    _browser.url = url

    logger.info("Browser %s started" % browser_name)

    def fin():
        _browser.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    # закрываем браузер после выполнения теста с выводом в лог
    request.addfinalizer(fin)
    return _browser
