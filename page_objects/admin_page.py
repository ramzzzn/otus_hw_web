from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminPage(BasePage):
    ADMIN_PROFILE = By.CSS_SELECTOR, "#nav-profile"
    ADMIN_LOGOUT = By.XPATH, "//*[text()='Logout']"
    MENU_CATALOG = By.CSS_SELECTOR, "#menu-catalog"
    MENU_PRODUCTS = By.XPATH, "//*[text()='Products']"

    def log_out(self):
        self.logger.info("Logout admin panel")
        # разлогин из админки
        self.click_action(self.ADMIN_LOGOUT)
        # проверка, что разлогин был выполнен
        self.wait_title("Administration")
        self.search_element((By.CSS_SELECTOR, "#input-username"))

    def open_admin_product_page(self):
        self.logger.info("Open => Product settings admin page")
        self.click_action(self.MENU_CATALOG)
        self.click_action(self.MENU_PRODUCTS)
