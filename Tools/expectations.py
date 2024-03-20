from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages import *


class Expectations:
    def __init__(self, driver):
        self.driver = driver

    def wait_title(self, title, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.title_is(title))
        except TimeoutException:
            # Выбрасываю своё исключение и добавляю сообщение
            raise AssertionError("Ждал что title будет: '{}' но он был '{}'".format(title, self.driver.title))

    def search_element(self, selector, timeout=1, by=By.CSS_SELECTOR):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, selector)))
        except TimeoutException:
            # self.driver.save_screenshot("{}.png".format(self.driver.session_id))
            raise AssertionError("Не дождался видимости элемента: {}".format(selector))

    def search_elements(self, selector, timeout=1, by=By.CSS_SELECTOR):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((by, selector)))
        except TimeoutException:
            raise AssertionError("Не дождался видимости элемента: {}".format(selector))

    def search_prices(self, selectors, timeout=1):
        prices = []
        for selector in selectors:
            elements_price = self.search_elements(selector, timeout)
            for element in elements_price:
                prices.append(element.text)
        return prices

    def search_prices_main_page(self, timeout=1):
        main_page_prices = self.search_prices(selectors=[MainPage.PRICE, MainPage.PRICE_TAX, MainPage.PRICE_OLD],
                                              timeout=timeout)
        return main_page_prices

    def search_prices_catalog_page(self, timeout=1):
        catalog_page_prices = self.search_prices(selectors=[CatalogPage.PRICE, CatalogPage.PRICE_TAX, CatalogPage.PRICE_OLD],
                                                 timeout=timeout)
        return catalog_page_prices
