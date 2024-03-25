import os

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
    parser.addoption("--base_url", action="store", default="http://172.22.144.70:8081")
    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption("--ya_driver", default="C:/otus_homeworks/homework_web/drivers/yandexdriver.exe")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--base_url")
    headless = request.config.getoption("--headless")
    ya_driver = request.config.getoption("--ya_driver")

    if browser_name == "chrome":
        service = ChromiumService()
        options = ChromiumOptions()
        if headless:
            options.add_argument("headless=new")
        _browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        service = FirefoxService()
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        _browser = webdriver.Firefox(service=service, options=options)
    elif browser_name == "edge":
        service = EdgeService()
        options = EdgeOptions()
        if headless:
            options.add_argument("headless=new")
        _browser = webdriver.Edge(service=service, options=options)
    elif browser_name == "yandex":
        service = ChromiumService(executable_path=ya_driver)
        options = ChromiumOptions()
        if headless:
            options.add_argument("headless=new")
        _browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "safari":
        service = SafariService()
        _browser = webdriver.Safari(service=service)

    _browser.maximize_window()
    request.addfinalizer(_browser.close)

    _browser.get(url)
    _browser.url = url

    return _browser
