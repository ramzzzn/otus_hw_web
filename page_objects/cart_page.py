from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    SHOPPING_CART = By.XPATH, "//*[@id='shopping-cart']"

    def get_product_name(self, product_name: str):
        self.search_element(locator=(By.XPATH, self.SHOPPING_CART[1] + self._text_xpath(text=product_name)))
