import pytest
from hamcrest import assert_that, equal_to, is_not, none

from helpers import generate_test_data_for_product, generate_test_data_for_user_registration
from page_objects import *
from page_elements import *


class TestScenarios:
    def test_admin_log_in_log_out(self, browser):
        # заходим на страничку авторизации
        LoginAdminPage(browser).open_login_admin_page()
        # логинимся в админку
        LoginAdminPage(browser).log_in_admin(username='user', password='bitnami')
        # разлогин из админки
        AdminPage(browser).log_out()

    def test_admin_add_delete_product(self, browser):
        # логинимся в админку
        LoginAdminPage(browser).open_login_admin_page().log_in_admin(username='user', password='bitnami')
        # переходим во вкладку Products
        AdminPage(browser).open_admin_product_page()
        # добавляем новый товар
        product_page = AdminProductPage(browser)
        product_page.open_product_add_page()
        test_product = generate_test_data_for_product()
        AdminAddProductPage(browser).add_new_product(**test_product)
        # проверяем что товар создан
        product_page.filter_by_product_name(product_name=test_product['product_name'])
        product_page.check_product_name_in_product_list(product_name=test_product['product_name'])
        product_page.get_model_name_from_product_list(model_name=test_product['model_name'])
        # удаляем созданный товар
        product_page.delete_product(product_name=test_product['product_name'])
        product_page.check_if_product_deleted(product_name=test_product['product_name'])
        # разлогин из админки
        AdminPage(browser).log_out()

    @pytest.mark.parametrize("product_name", ['MacBook', 'iPhone'])
    def test_add_to_cart(self, browser, product_name):
        # заходим на главную страницу
        MainPage(browser).open_main_page()
        # добавляем товар в корзину
        MainPage(browser).add_to_cart_by_product_name(product_name)
        # проверяем, что товар добавлен в корзину
        AlertElement(browser).shopping_cart.click()
        CartPage(browser).get_product_name(product_name)

    def test_change_currency_main_page(self, browser):
        # заходим на главную страницу
        MainPage(browser).open_main_page()
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
        MainPage(browser).open_main_page()
        MainPage(browser).open_desktops_catalog_page()
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

    def test_user_registration(self, browser):
        # заходим на главную страницу и открываем страницу регистрации пользователя
        MainPage(browser).open_main_page()
        MainPage(browser).open_user_registration_page()
        # регистрируем нового пользователя
        test_user = generate_test_data_for_user_registration()
        UserRegistrationPage(browser).register_user(**test_user)
        # логинимся под новым пользователем
        UserRegistrationPage(browser).user_logout()
        MainPage(browser).open_user_login_page()
        UserLoginPage(browser).login_user(email=test_user['email'], password=test_user['password'])
