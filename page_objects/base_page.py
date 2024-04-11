from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def _text_xpath(self, text: str):
        return f"//*[text()='{text}']"

    def open_page(self, page: str):
        self.browser.get(f"{self.browser.url}{page}")

    def wait_title(self, title: str, timeout: int = 3):
        try:
            WebDriverWait(self.browser, timeout).until(EC.title_is(title))
        except TimeoutException:
            raise AssertionError(f"Ждал что title будет: '{title}' но он был '{self.browser.title}'")

    def search_element(self, locator: tuple, timeout: int = 1):
        try:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            # self.driver.save_screenshot("{}.png".format(self.driver.session_id))
            raise TimeoutException(f"Не дождался видимости элемента: {locator}")

    def search_elements(self, locator: tuple, timeout=1):
        try:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Не найден ни один элемент по указанному селектору: {locator}")

    def click_action(self, locator: tuple, timeout: int = 1):
        ActionChains(self.browser)\
            .pause(0.5).move_to_element(self.search_element(locator, timeout))\
            .pause(0.5).click()\
            .perform()

    def input(self, locator: tuple, text: str):
        self.search_element(locator).click()
        self.search_element(locator).clear()
        for letter in text:
            self.search_element(locator).send_keys(letter)
        return self
