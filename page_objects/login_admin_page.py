from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoginAdminPage(BasePage):
    USERNAME_INPUT = By.CSS_SELECTOR, "#input-username"
    PASSWORD_INPUT = By.CSS_SELECTOR, "#input-password"
    SUBMIT_BUTTON = By.CSS_SELECTOR, "button[type='submit']"
    OPENCART_LINK = By.CSS_SELECTOR, "footer > a[href='https://www.opencart.com']"
    IMG_LOGO = By.CSS_SELECTOR, "img[title='OpenCart']"
    ADMIN_PROFILE = By.CSS_SELECTOR, "#nav-profile"
    ADMIN_LOGOUT = By.CSS_SELECTOR, "#nav-logout"


    def open_login_admin_page(self):
        self.open_page('/administration')
        self.wait_title("Administration")

    def log_in_admin(self, username: str, password: str):
        # логинимся в админку
        self.input(self.USERNAME_INPUT, username)
        self.input(self.PASSWORD_INPUT, password)
        self.click_action(self.SUBMIT_BUTTON)
        # проверка, что логин был выполнен
        self.wait_title("Dashboard")
        self.search_element(self.ADMIN_PROFILE)

    def log_out_admin(self):
        # разлогин из админки
        self.click_action(self.ADMIN_LOGOUT)
        # проверка, что разлогин был выполнен
        self.wait_title("Administration")
        self.search_element(self.USERNAME_INPUT)

