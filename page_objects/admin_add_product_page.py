from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminAddProductPage(BasePage):
    BUTTON_SAVE = By.CSS_SELECTOR, ".float-end > button"
    BUTTON_BACK = By.CSS_SELECTOR, ".float-end > a"
    TAB_GENERAL = By.CSS_SELECTOR, "[href='#tab-general']"
    TAB_DATA = By.CSS_SELECTOR, "[href='#tab-data']"
    TAB_SEO = By.CSS_SELECTOR, "[href='#tab-seo']"
    INPUT_MODEL = By.CSS_SELECTOR, "#input-model"
    INPUT_KEYWORD = By.CSS_SELECTOR, "#input-keyword-0-1"
    INPUT_PRODUCT_NAME = By.CSS_SELECTOR, "#input-name-1"
    INPUT_META_TAG_TITLE = By.CSS_SELECTOR, "#input-meta-title-1"

    def _save_product(self):
        self.click_action(self.BUTTON_SAVE)
        self.click_action(self.BUTTON_BACK)

    def _set_general_properties(self, product_name: str, meta_tag_title: str):
        self.click_action(self.TAB_GENERAL)
        self.input(self.INPUT_PRODUCT_NAME, product_name)
        self.input(self.INPUT_META_TAG_TITLE, meta_tag_title)

    def _set_data_properties(self, model_name: str):
        self.click_action(self.TAB_DATA)
        self.input(self.INPUT_MODEL, model_name)

    def _set_seo_properties(self, keyword: str):
        self.click_action(self.TAB_SEO)
        self.input(self.INPUT_KEYWORD, keyword)

    def add_new_product(self, product_name: str, meta_tag_title: str, model_name: str, keyword: str):
        self.logger.info("Adding new product")
        self._set_general_properties(product_name, meta_tag_title)
        self._set_data_properties(model_name)
        self._set_seo_properties(keyword)
        self._save_product()
