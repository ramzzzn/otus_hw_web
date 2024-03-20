from hamcrest import assert_that, contains_string, equal_to, is_not
from selenium.webdriver import ActionChains
from Tools.expectations import Expectations
from pages import *


class TestScenarios:
    def test_admin_log_in_log_out(self, browser):
        exp = Expectations(browser)
        browser.get(f"{browser.url}/administration")
        exp.wait_title("Administration")
        # логин в админку
        exp.search_element(LoginAdminPage.USERNAME_INPUT).send_keys(LoginAdminPage.USERNAME)
        exp.search_element(LoginAdminPage.PASSWORD_INPUT).send_keys(LoginAdminPage.PASSWORD)
        exp.search_element(LoginAdminPage.SUBMIT_BUTTON).click()
        # проверка, что логин был выполнен
        exp.wait_title("Dashboard")
        exp.search_element("#nav-profile")
        # разлогин из админки
        exp.search_element("#nav-logout").click()
        # проверка, что разлогин был выполнен
        exp.wait_title("Administration")
        exp.search_element(LoginAdminPage.USERNAME_INPUT)

    def test_add_to_cart(self, browser):
        exp = Expectations(browser)
        browser.get(f"{browser.url}/home")
        actions = ActionChains(browser, duration=0)
        exp.wait_title("Your Store")
        # добавляем товар в корзину
        add_to_cart = exp.search_element(MainPage.ADD_TO_CART_BUTTON)
        actions.move_to_element(add_to_cart).click().perform()
        # проверяем, что товар добавлен в корзину
        exp.search_element("div.alert-success")
        shopping_cart = exp.search_element(MainPage.SHOPPING_CART_BUTTON)
        actions.move_to_element(shopping_cart).click().perform()
        exp.search_element("table.table-striped.mb-2 a[href*='/product/']")

    def test_change_currency_main_page(self, browser):
        exp = Expectations(browser)
        browser.get(f"{browser.url}/home")
        exp.wait_title("Your Store")
        # получаем все цены до смены валюты
        dollar_prices = exp.search_prices_main_page()
        # меняем валюту на евро
        exp.search_element(MainPage.CURRENCY_TAB).click()
        exp.search_element(MainPage.CURRENCY_EUR).click()
        euro_prices = exp.search_prices_main_page(timeout=2)
        # проверяем, что цены поменялись и указаны в евро
        n = 0
        while n < len(euro_prices):
            assert_that(euro_prices[n], contains_string('€'), "Валюта у цены не поменялась")
            assert_that(euro_prices[n], is_not(equal_to(dollar_prices[n])), "Цена товара не поменялась")
            n += 1

    def test_change_currency_catalog_page(self, browser):
        exp = Expectations(browser)
        browser.get(f"{browser.url}/en-gb/catalog/desktops")
        exp.wait_title("Desktops")
        # получаем все цены до смены валюты
        dollar_prices = exp.search_prices_catalog_page()
        # меняем валюту на евро
        exp.search_element(CatalogPage.CURRENCY_TAB).click()
        exp.search_element(CatalogPage.CURRENCY_EUR).click()
        euro_prices = exp.search_prices_catalog_page(timeout=2)
        # проверяем, что цены поменялись и указаны в евро
        n = 0
        while n < len(euro_prices):
            assert_that(euro_prices[n], contains_string('€'), "Валюта у цены не поменялась")
            assert_that(euro_prices[n], is_not(equal_to(dollar_prices[n])), "Цена товара не поменялась")
            n += 1
