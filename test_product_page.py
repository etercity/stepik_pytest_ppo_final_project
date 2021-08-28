import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
promo_codes = ['?promo=offer'+str(code) for code in range(0,10)]
promo_links = [url+promo for promo in promo_codes]
promo_links[7] = pytest.param(promo_links[7], marks=pytest.mark.skip)


# @pytest.mark.parametrize('promo_link', promo_links)
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    product_name = page.get_product_name()
    price = page.get_price()
    page.add_to_basket()
    # time.sleep(10)

    page.should_be_product_name(product_name=product_name)  # проверка соответствия имени товара в корзине
    page.should_be_price(price=price)   # проверка соответствия цены товара в корзине

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()    # проверяем, что нет сообщения об успехе

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()    # проверяем, что нет сообщения об успехе

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_in_header()       # переходим в корзину из шапки
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty() # Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty_basket_message()    # Ожидаем, что есть текст о том что корзина пуста


class TestUserAddToBasketFromProductPage():
    # @pytest.mark.skip
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message()  # проверяем, что нет сообщения об успехе

    # @pytest.mark.skip
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, url)
        page.open()
        product_name = page.get_product_name()
        price = page.get_price()
        page.add_to_basket()
        # time.sleep(10)

        page.should_be_product_name(product_name=product_name)  # проверка соответствия имени товара в корзине
        page.should_be_price(price=price)  # проверка соответствия цены товара в корзине


