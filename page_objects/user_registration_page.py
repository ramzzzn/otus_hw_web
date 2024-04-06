from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class UserRegistrationPage(BasePage):
    LOGIN_PAGE_LINK = By.XPATH, "//*[text()='login page']"
    FIRST_NAME_INPUT = By.CSS_SELECTOR, "#input-firstname"
    LAST_NAME_INPUT = By.CSS_SELECTOR, "#input-lastname"
    E_MAIL_INPUT = By.CSS_SELECTOR, "#input-email"
    PASSWORD_INPUT = By.CSS_SELECTOR, "#input-password"
    NEWSLETTER_CHECKBOX = By.CSS_SELECTOR, "#input-newsletter"
    PRIVACY_POLICY_LINK = By.CSS_SELECTOR, "input[name='agree']"
    CONTINUE_BUTTON = By.XPATH, "//button[text()='Continue']"
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

    def open_user_registration_page(self):
        self.open_page('/en-gb?route=account/register')
        self.wait_title("Register Account")
