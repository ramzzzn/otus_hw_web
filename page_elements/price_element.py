from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class PriceElement:
    PRICE = By.CSS_SELECTOR, "span.price-new"
    PRICE_TAX = By.CSS_SELECTOR, "span.price-tax"
    PRICE_OLD = By.CSS_SELECTOR, "span.price-old"

    def __init__(self, browser):
        self.browser = browser

    def _search_elements(self, locator, timeout=1):
        try:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не найден ни один элемент по указанному селектору: {locator}")

    def search_prices(self, timeout=1):
        return self._search_elements(self.PRICE, timeout)

    def search_tax_prices(self, timeout=1):
        return self._search_elements(self.PRICE_TAX, timeout)

    def search_old_prices(self, timeout=1):
        return self._search_elements(self.PRICE_OLD, timeout)
