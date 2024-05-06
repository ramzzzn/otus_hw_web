import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    SHOPPING_CART = By.XPATH, "//*[@id='shopping-cart']"

    @allure.step("Проверяю наличие продукта {product_name} в корзине")
    def check_product_in_cart(self, product_name: str):
        self.logger.info("Checking that product added to the cart")
        self.search_element(locator=(By.XPATH, self.SHOPPING_CART[1] + self._text_xpath(text=product_name)))
