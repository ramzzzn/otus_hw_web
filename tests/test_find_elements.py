from page_objects import *
import os
os.environ["PATH"] += ";C:\\path\\to\\your\\executable"


class TestFindElements:
    def test_main_page(self, browser):
        exp = MainPage(browser)
        exp.open_main_page()
        exp.search_element(exp.INPUT_SEARCH)
        exp.search_element(exp.BUTTON_SEARCH)
        exp.search_element(exp.BUTTON_SHOPPING_CART)
        exp.search_element(exp.CAROUSEL_BANNER)
        exp.search_element(exp.CARD_PAGE_IPHONE)

    def test_laptops_catalog_page(self, browser):
        MainPage(browser).open_main_page()
        MainPage(browser).open_desktops_catalog_page()
        exp = CatalogPage(browser)
        exp.search_element(CatalogPage.LIST_GROUP_ITEM_DESKTOPS)
        exp.search_element(CatalogPage.LIST_GROUP_ITEM_LAPTOPS_NOTEBOOKS)
        exp.search_element(CatalogPage.LIST_GROUP_ITEM_COMPONENTS)
        exp.search_element(CatalogPage.LIST_GROUP_ITEM_TABLETS)
        exp.search_element(CatalogPage.LIST_GROUP_ITEM_SOFTWARE)
        exp.search_element(CatalogPage.LIST_GROUP_ITEM_PHONES_PDA)
        exp.search_element(CatalogPage.LIST_GROUP_ITEM_CAMERAS)
        exp.search_element(CatalogPage.LIST_GROUP_ITEM_MP3_PLAYERS)
        exp.search_element(CatalogPage.COMPARE_BUTTON)
        exp.search_element(CatalogPage.LIST_VIEW_BUTTON)
        exp.search_element(CatalogPage.GRID_VIEW_BUTTON)
        exp.search_element(CatalogPage.SELECT_SORT)
        exp.search_element(CatalogPage.SELECT_SHOW_LIMIT)
        exp.search_element(CatalogPage.REFINE_SEARCH_MAC)
        exp.search_element(CatalogPage.REFINE_SEARCH_PC)

    def test_product_card_page(self, browser):
        MainPage(browser).open_main_page()
        MainPage(browser).open_product_card_page()
        exp = ProductCardPage(browser)
        exp.search_element(ProductCardPage.MAIN_PRODUCT_IMG)
        exp.search_element(ProductCardPage.PRICE)
        exp.search_element(ProductCardPage.WISH_LIST_BUTTON)
        exp.search_element(ProductCardPage.INPUT_QUANTITY)
        exp.search_element(ProductCardPage.TAB_REVIEW)
        exp.search_element(ProductCardPage.DESCRIPTION)

    def test_login_admin_page(self, browser):
        exp = LoginAdminPage(browser)
        exp.open_login_admin_page()
        exp.search_element(LoginAdminPage.USERNAME_INPUT)
        exp.search_element(LoginAdminPage.PASSWORD_INPUT)
        exp.search_element(LoginAdminPage.SUBMIT_BUTTON)
        exp.search_element(LoginAdminPage.OPENCART_LINK)
        exp.search_element(LoginAdminPage.IMG_LOGO)

    def test_user_registration_page(self, browser):
        MainPage(browser).open_main_page()
        MainPage(browser).open_user_registration_page()
        exp = UserRegistrationPage(browser)
        exp.search_element(UserRegistrationPage.LOGIN_PAGE_LINK)
        exp.search_element(UserRegistrationPage.INPUT_FIRST_NAME)
        exp.search_element(UserRegistrationPage.INPUT_EMAIL)
        exp.search_element(UserRegistrationPage.INPUT_PASSWORD)
        exp.search_element(UserRegistrationPage.CHECKBOX_NEWSLETTER)
        exp.search_element(UserRegistrationPage.CHECKBOX_PRIVACY_POLICY)
        exp.search_element(UserRegistrationPage.BUTTON_CONTINUE)
        exp.search_element(UserRegistrationPage.LIST_GROUP_ITEM_LOGIN)
        exp.search_element(UserRegistrationPage.LIST_GROUP_ITEM_REGISTER)
        exp.search_element(UserRegistrationPage.LIST_GROUP_ITEM_FORGOTTEN_PASSWORD)
        exp.search_element(UserRegistrationPage.LIST_GROUP_ITEM_MY_ACCOUNT)
        exp.search_element(UserRegistrationPage.LIST_GROUP_ITEM_ADDRESS_BOOK)
        exp.search_element(UserRegistrationPage.LIST_GROUP_ITEM_WISHLIST)
        exp.search_element(UserRegistrationPage.LIST_GROUP_ITEM_ORDER)
        exp.search_element(UserRegistrationPage.LIST_GROUP_ITEM_DOWNLOAD)
        exp.search_element(UserRegistrationPage.LIST_GROUP_ITEM_SUBSCRIPTION)
        exp.search_element(UserRegistrationPage.LIST_GROUP_ITEM_REWARD)
        exp.search_element(UserRegistrationPage.LIST_GROUP_ITEM_RETURNS)
        exp.search_element(UserRegistrationPage.LIST_GROUP_ITEM_TRANSACTION)
        exp.search_element(UserRegistrationPage.LIST_GROUP_ITEM_NEWSLETTER)
