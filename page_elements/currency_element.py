import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CurrencyElement:
    CURRENCY_MENU = (By.CSS_SELECTOR, "#form-currency")
    CURRENCY_USD = (By.CSS_SELECTOR, "a.dropdown-item[href='USD']")
    CURRENCY_EUR = (By.CSS_SELECTOR, "a.dropdown-item[href='EUR']")
    CURRENCY_GBP = (By.CSS_SELECTOR, "a.dropdown-item[href='GBP']")

    def __init__(self, browser):
        self.browser = browser
        self.currency_menu = WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(self.CURRENCY_MENU))

    def _select_currency(self, currency_locator):
        self.currency_menu.click()
        try:
            WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(currency_locator)).click()
        except TimeoutException:
            raise AssertionError(f"Не найден ни один элемент по указанному селектору: {currency_locator}")

    @allure.step("Выполняю смену валюты на USD")
    def switch_currency_to_usd(self):
        self._select_currency(self.CURRENCY_USD)

    @allure.step("Выполняю смену валюты на EUR")
    def switch_currency_to_eur(self):
        self._select_currency(self.CURRENCY_EUR)

    @allure.step("Выполняю смену валюты на GBP")
    def switch_currency_to_gbp(self):
        self._select_currency(self.CURRENCY_GBP)
