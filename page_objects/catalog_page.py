from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    LIST_GROUP_ITEM_DESKTOPS = By.CSS_SELECTOR, "a.list-group-item[href='http://172.22.144.70:8081/en-gb/catalog/desktops']"
    LIST_GROUP_ITEM_LAPTOPS_NOTEBOOKS = By.CSS_SELECTOR, "a.list-group-item[href='http://172.22.144.70:8081/en-gb/catalog/laptop-notebook']"
    LIST_GROUP_ITEM_COMPONENTS = By.CSS_SELECTOR, "a.list-group-item[href='http://172.22.144.70:8081/en-gb/catalog/component']"
    LIST_GROUP_ITEM_TABLETS = By.CSS_SELECTOR, "a.list-group-item[href='http://172.22.144.70:8081/en-gb/catalog/tablet']"
    LIST_GROUP_ITEM_SOFTWARE = By.CSS_SELECTOR, "a.list-group-item[href='http://172.22.144.70:8081/en-gb/catalog/software']"
    LIST_GROUP_ITEM_PHONES_PDA = By.CSS_SELECTOR, "a.list-group-item[href='http://172.22.144.70:8081/en-gb/catalog/smartphone']"
    LIST_GROUP_ITEM_CAMERAS = By.CSS_SELECTOR, "a.list-group-item[href='http://172.22.144.70:8081/en-gb/catalog/cameras']"
    LIST_GROUP_ITEM_MP3_PLAYERS = By.CSS_SELECTOR, "a.list-group-item[href='http://172.22.144.70:8081/en-gb/catalog/mp3-players']"
    COMPARE_BUTTON = By.CSS_SELECTOR, "#compare-total"
    LIST_VIEW_BUTTON = By.CSS_SELECTOR, "#button-list"
    GRID_VIEW_BUTTON = By.CSS_SELECTOR, "#button-grid"
    SELECT_SORT = By.CSS_SELECTOR, "#input-sort"
    SELECT_SHOW_LIMIT = By.CSS_SELECTOR, "#input-limit"
    REFINE_SEARCH_MAC = By.CSS_SELECTOR, "div.col-sm-3 a[href*='/desktops/mac']"
    REFINE_SEARCH_PC = By.CSS_SELECTOR, "div.col-sm-3 a[href*='/desktops/pc']"
    PRICE = By.CSS_SELECTOR, "span.price-new"
    PRICE_TAX = By.CSS_SELECTOR, "span.price-tax"
    PRICE_OLD = By.CSS_SELECTOR, "span.price-old"
    CURRENCY_TAB = By.CSS_SELECTOR, "#form-currency"
    CURRENCY_EUR = By.CSS_SELECTOR, "a.dropdown-item[href='EUR']"
