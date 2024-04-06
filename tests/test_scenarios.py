from hamcrest import assert_that, equal_to, is_not
from page_objects import *
from page_elements import *


class TestScenarios:
    def test_admin_log_in_log_out(self, browser):
        # заходим на страничку авторизации
        exp = LoginAdminPage(browser)
        exp.open_login_admin_page()
        # логинимся в админку
        exp.log_in_admin(username='user', password='bitnami')
        # разлогин из админки
        exp.log_out_admin()

    def test_add_to_cart(self, browser):
        # заходим на главную страницу
        exp = MainPage(browser)
        exp.open_main_page()
        # добавляем товар в корзину
        exp.add_product_to_cart()
        # проверяем, что товар добавлен в корзину
        AlertElement(browser).shopping_cart.click()
        CartPage(browser).get_product_name(product_name='MacBook')

    def test_change_currency_main_page(self, browser):
        # заходим на главную страницу
        exp = MainPage(browser)
        exp.open_main_page()
        # получаем все цены до смены валюты
        prices = PriceElement(browser)
        dollar_prices = prices.search_prices()
        dollar_tax_prices = prices.search_tax_prices()
        dollar_old_prices = prices.search_old_prices()
        # меняем валюту на евро
        CurrencyElement(browser).switch_currency_to_eur()
        euro_prices = prices.search_prices()
        euro_tax_prices = prices.search_tax_prices()
        euro_old_prices = prices.search_old_prices()
        # проверяем, что цены поменялись и указаны в евро
        assert_that(euro_prices, is_not(equal_to(dollar_prices)), "Цены на товары не поменялись")
        assert_that(euro_tax_prices, is_not(equal_to(dollar_tax_prices)), "Цены без налога на товары не поменялись")
        assert_that(euro_old_prices, is_not(equal_to(dollar_old_prices)), "Старые цены на товары не поменялись")

    def test_change_currency_catalog_page(self, browser):
        # заходим на главную страницу
        exp = CatalogPage(browser)
        exp.open_catalog_page()
        # получаем все цены до смены валюты
        prices = PriceElement(browser)
        dollar_prices = prices.search_prices()
        dollar_tax_prices = prices.search_tax_prices()
        dollar_old_prices = prices.search_old_prices()
        # меняем валюту на евро
        CurrencyElement(browser).switch_currency_to_eur()
        euro_prices = prices.search_prices()
        euro_tax_prices = prices.search_tax_prices()
        euro_old_prices = prices.search_old_prices()
        # проверяем, что цены поменялись и указаны в евро
        assert_that(euro_prices, is_not(equal_to(dollar_prices)), "Цены на товары не поменялись")
        assert_that(euro_tax_prices, is_not(equal_to(dollar_tax_prices)), "Цены без налога на товары не поменялись")
        assert_that(euro_old_prices, is_not(equal_to(dollar_old_prices)), "Старые цены на товары не поменялись")
