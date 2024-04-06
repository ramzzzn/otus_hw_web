from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertElement:
    SUCCESS_ALERT = By.CSS_SELECTOR, ".alert-success"
    SHOPPING_CART_LINK = By.CSS_SELECTOR, "div > [href$='/en-gb?route=checkout/cart']"

    def __init__(self, browser):
        self.browser = browser
        self.alert = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.SUCCESS_ALERT))

    @property
    def shopping_cart(self):
        return self.alert.find_element(*self.SHOPPING_CART_LINK)
