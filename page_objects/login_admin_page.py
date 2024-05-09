import allure
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

    @allure.step("Открываю страницу авторизации в раздел администратора")
    def open_login_admin_page(self):
        self.logger.info("Login as admin")
        self.open_page('/administration')
        self.wait_title("Administration")
        return self

    @allure.step("Авторизуюсь в раздел администратора")
    def log_in_admin(self, username: str, password: str):
        self.logger.info("Login to the admin panel")
        # логинимся в админку
        self.input(self.USERNAME_INPUT, username)
        self.input(self.PASSWORD_INPUT, password)
        self.click_action(self.SUBMIT_BUTTON)
        # проверка, что логин был выполнен
        self.wait_title("Dashboard")
        self.search_element((By.CSS_SELECTOR, "#nav-profile"))
        return self
