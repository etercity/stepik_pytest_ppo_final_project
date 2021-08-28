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
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    product_name = page.get_product_name()
    price = page.get_price()
    page.add_to_basket()

    page.should_be_product_name(product_name=product_name)  # проверка соответствия имени товара в корзине
    page.should_be_price(price=price)   # проверка соответствия цены товара в корзине

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_in_header()       # переходим в корзину из хедера
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty() # в корзине не должно быть товаров
    basket_page.should_be_empty_basket_message()    # сообщение о том что корзина пуста

@pytest.mark.user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + "@mail.com", 'qwern985ombg')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message()  # сешн ерор

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, url)
        page.open()
        product_name = page.get_product_name()
        price = page.get_price()
        page.add_to_basket()

        page.should_be_product_name(product_name=product_name)  # валидация имени товара в корзине
        page.should_be_price(price=price)   # валидация цены товара в корзине
