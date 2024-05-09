from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ProductCardPage(BasePage):
    MAIN_PRODUCT_IMG = By.CSS_SELECTOR, "img.img-thumbnail.mb-3"
    PRICE = By.CSS_SELECTOR, "ul.list-unstyled  span.price-new"
    WISH_LIST_BUTTON = By.CSS_SELECTOR, "button.btn.btn-light[formaction$='/wishlist.add']"
    INPUT_QUANTITY = By.CSS_SELECTOR, "#input-quantity"
    TAB_REVIEW = By.CSS_SELECTOR, "a.nav-link[href='#tab-review']"
    TAB_DESCRIPTION = By.CSS_SELECTOR, "a.nav-link[href='#tab-description']"
    DESCRIPTION = By.CSS_SELECTOR, "#tab-description[role='tabpanel']"
