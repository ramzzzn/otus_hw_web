from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminProductPage(BasePage):
    BUTTON_ADD_NEW_PRODUCT = By.CSS_SELECTOR, "div.float-end > a"
    BUTTON_DELETE_PRODUCT = By.CSS_SELECTOR, "button.btn-danger"
    BUTTON_FILTER = By.CSS_SELECTOR, "button#button-filter"
    PRODUCT_CHECKBOX = By.CSS_SELECTOR, "[name='selected[]']"
    INPUT_PRODUCT_NAME = By.CSS_SELECTOR, "input#input-name"

    def _td_text_xpath(self, text: str):
        return f"//td[contains(text(), '{text}')]"

    def open_product_add_page(self):
        self.logger.info("Open => Product add page")
        self.click_action(self.BUTTON_ADD_NEW_PRODUCT)

    def filter_by_product_name(self, product_name: str):
        self.logger.info("Filter products by product name")
        self.input(self.INPUT_PRODUCT_NAME, product_name)
        self.click_action(self.BUTTON_FILTER)

    def _get_parameter_from_product_list(self, value: str, retry=3):
        for i in range(1, retry):
            try:
                return self.search_element(locator=(By.XPATH, self._td_text_xpath(value))).text
            except StaleElementReferenceException:
                continue

    def check_product_name_in_product_list(self, product_name):
        self.logger.info("Checking product in product list")
        result = self._get_parameter_from_product_list(value=product_name)
        if result:
            return result.split()[0]
        else:
            return None

    def get_model_name_from_product_list(self, model_name):
        self.logger.info("Checking model in product list")
        return self._get_parameter_from_product_list(value=model_name)

    def _select_product_by_product_name(self, product_name: str):
        self.click_action(locator=(By.XPATH, self._td_text_xpath(text=product_name) +
                                   "/preceding-sibling::td/input[@type='checkbox']"))

    def delete_product(self, product_name: str):
        self.logger.info("Deleting product")
        self._select_product_by_product_name(product_name)
        self.click_action(self.BUTTON_DELETE_PRODUCT)
        confirm_delete = self.browser.switch_to.alert
        confirm_delete.accept()

    def check_if_product_deleted(self, product_name: str):
        self.logger.info("Checking if product deleted")
        self.filter_by_product_name(product_name)
        self.search_element(locator=(By.XPATH, self._td_text_xpath(text='No results!')))
        self.logger.info("Product was succesfully deleted")
