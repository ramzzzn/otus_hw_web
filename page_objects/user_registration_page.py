import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class UserRegistrationPage(BasePage):
    LOGIN_PAGE_LINK = By.XPATH, "//*[text()='login page']"
    INPUT_FIRST_NAME = By.CSS_SELECTOR, "#input-firstname"
    INPUT_LAST_NAME = By.CSS_SELECTOR, "#input-lastname"
    INPUT_EMAIL = By.CSS_SELECTOR, "#input-email"
    INPUT_PASSWORD = By.CSS_SELECTOR, "#input-password"
    CHECKBOX_NEWSLETTER = By.CSS_SELECTOR, "#input-newsletter"
    CHECKBOX_PRIVACY_POLICY = By.CSS_SELECTOR, "input[name='agree']"
    BUTTON_CONTINUE = By.XPATH, "//*[text()='Continue']"
    LIST_GROUP_ITEM_LOGIN = By.CSS_SELECTOR, "a.list-group-item[href*='/login']"
    LIST_GROUP_ITEM_REGISTER = By.CSS_SELECTOR, "a.list-group-item[href*='/register']"
    LIST_GROUP_ITEM_FORGOTTEN_PASSWORD = By.CSS_SELECTOR, "a.list-group-item[href*='/forgotten']"
    LIST_GROUP_ITEM_MY_ACCOUNT = By.CSS_SELECTOR, "a.list-group-item[href*='/account']"
    LIST_GROUP_ITEM_ADDRESS_BOOK = By.CSS_SELECTOR, "a.list-group-item[href*='/address']"
    LIST_GROUP_ITEM_WISHLIST = By.CSS_SELECTOR, "a.list-group-item[href*='/wishlist']"
    LIST_GROUP_ITEM_ORDER = By.CSS_SELECTOR, "a.list-group-item[href*='/order']"
    LIST_GROUP_ITEM_DOWNLOAD = By.CSS_SELECTOR, "a.list-group-item[href*='/download']"
    LIST_GROUP_ITEM_SUBSCRIPTION = By.CSS_SELECTOR, "a.list-group-item[href*='/subscription']"
    LIST_GROUP_ITEM_REWARD = By.CSS_SELECTOR, "a.list-group-item[href*='/reward']"
    LIST_GROUP_ITEM_RETURNS = By.CSS_SELECTOR, "a.list-group-item[href*='/returns']"
    LIST_GROUP_ITEM_TRANSACTION = By.CSS_SELECTOR, "a.list-group-item[href*='/transaction']"
    LIST_GROUP_ITEM_NEWSLETTER = By.CSS_SELECTOR, "a.list-group-item[href*='/newsletter']"
    LIST_GROUP_ITEM_LOGOUT = By.XPATH, "//div/a[text()='Logout']"

    @allure.step("Регистрирую пользователя {first_name} с email {email}")
    def register_user(self, first_name: str, last_name: str, email: str, password: str):
        self.logger.info("Registering a new user")
        self.input(self.INPUT_FIRST_NAME, first_name)
        self.input(self.INPUT_LAST_NAME, last_name)
        self.input(self.INPUT_EMAIL, email)
        self.input(self.INPUT_PASSWORD, password)
        self.click_action(self.CHECKBOX_PRIVACY_POLICY)
        self.click_action(self.BUTTON_CONTINUE)
        self.wait_title("Your Account Has Been Created!")

    @allure.step("Выполняю выход пользователя из системы")
    def user_logout(self):
        self.logger.info("Logout a user")
        self.click_action(self.LIST_GROUP_ITEM_LOGOUT)
        self.click_action(self.BUTTON_CONTINUE)
        self.wait_title("Your Store")
