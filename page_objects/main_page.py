from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class MainPage(BasePage):
    CURRENCY_TAB = By.CSS_SELECTOR, "#form-currency"
    CURRENCY_USD = By.CSS_SELECTOR, "a.dropdown-item[href='USD']"
    CURRENCY_EUR = By.CSS_SELECTOR, "a.dropdown-item[href='EUR']"
    CURRENCY_GBP = By.CSS_SELECTOR, "a.dropdown-item[href='GBP']"
    SEARCH_INPUT = By.CSS_SELECTOR, "#search"
    SEARCH_BUTTON = By.CSS_SELECTOR, "button.btn-light"
    SHOPPING_CART_BUTTON = By.CSS_SELECTOR, "button.dropdown-toggle"
    MENU_BAR = By.CSS_SELECTOR, "#menu"
    PRICE = By.CSS_SELECTOR, "span.price-new"
    PRICE_TAX = By.CSS_SELECTOR, "span.price-tax"
    PRICE_OLD = By.CSS_SELECTOR, "span.price-old"
    CAROUSEL_BANNER = By.CSS_SELECTOR, "#carousel-banner-0"
    ADD_TO_CART_BUTTON = By.CSS_SELECTOR, "i.fa-shopping-cart"
    IPHONE_IMG = By.CSS_SELECTOR, "img[title='iPhone']"

    def open_main_page(self):
        self.open_page('/home')
        self.wait_title("Your Store")

    def add_product_to_cart(self, index: int = 0):
        if index == 0:
            self.click_action(self.ADD_TO_CART_BUTTON)
        else:
            self.search_element(self.ADD_TO_CART_BUTTON)[index].click()
