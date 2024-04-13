from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class MainPage(BasePage):
    INPUT_SEARCH = By.CSS_SELECTOR, "#search"
    BUTTON_SEARCH = By.CSS_SELECTOR, "button.btn-light"
    BUTTON_SHOPPING_CART = By.CSS_SELECTOR, "button.dropdown-toggle"
    BUTTON_ADD_TO_CART = "//i[contains(@class, 'fa-solid fa-shopping-cart')]"
    CAROUSEL_BANNER = By.CSS_SELECTOR, "#carousel-banner-0"
    MENU_DESKTOP = By.XPATH, "//a[text()='Desktops']"
    MENU_DESKTOP_SHOW_ALL = By.XPATH, "//a[text()='Show All Desktops']"
    MENU_MY_ACCOUNT = By.XPATH, "//span[text()='My Account']"
    MENU_MY_ACCOUNT_REGISTER = By.XPATH, "//a[text()='Register']"
    MENU_MY_ACCOUNT_LOGIN = By.XPATH, "//a[text()='Login']"
    CARD_PAGE_IPHONE = By.CSS_SELECTOR, "img[title='iPhone']"

    def open_main_page(self):
        self.logger.info("Open => Main page")
        self.open_page('/home')
        self.wait_title("Your Store")

    def open_desktops_catalog_page(self):
        self.logger.info("Open => Desktops catalog")
        self.click_action(self.MENU_DESKTOP)
        self.click_action(self.MENU_DESKTOP_SHOW_ALL)
        self.wait_title("Desktops")

    def open_user_registration_page(self):
        self.logger.info("Open => User registration page")
        self.click_action(self.MENU_MY_ACCOUNT)
        self.click_action(self.MENU_MY_ACCOUNT_REGISTER)
        self.wait_title("Register Account")

    def open_user_login_page(self):
        self.logger.info("Open => User login page")
        self.click_action(self.MENU_MY_ACCOUNT)
        self.click_action(self.MENU_MY_ACCOUNT_LOGIN)
        self.wait_title("Account Login")

    def open_product_card_page(self):
        self.logger.info("Open => iPhone card page")
        self.click_action(self.CARD_PAGE_IPHONE)
        self.wait_title("iPhone")

    def add_to_cart_by_product_name(self, product_name):
        self.logger.info("Add product %s to cart" % product_name)
        self.click_action(locator=(By.XPATH, f"//div[h4/a[text()='{product_name}']]/following-sibling::form" +
                                   self.BUTTON_ADD_TO_CART))

    # def add_product_to_cart(self, index: int = 0):
    #     if index == 0:
    #         self.click_action(self.BUTTON_ADD_TO_CART)
    #     else:
    #         self.search_element(self.BUTTON_ADD_TO_CART)[index].click()
