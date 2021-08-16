from .base_page import BasePage
from .locators import  ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        """ Получает имя товара, добавляемого в корзину """
        product_name = self.browser.find_element(*ProductPageLocators.PRUDUCT_NAME).text
        return product_name

    def get_price(self):
        """ Получает цену товара, добавляемого в корзину """
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        return price

    def add_to_basket(self):
        """ Добавляет товар в корзину """
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()


    def should_be_product_name(self,product_name):
        """ Проверяет соответствие названия товара в корзине """
        assert product_name == self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text,\
        'Product name is not correct!'

    def should_be_price(self, price):
        """ Проверяет соответствие цены товара в корзине """
        assert price == self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text,\
        'Product price is not correct!'

    def should_not_be_success_message(self):
        """ Проверяет, что элемент отсутствует на странице """
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        """ Проверяет, что элемент исчез со страницы (вообще лучше проверять в два приёма:
         сначала проверить, что он был, а потом что его не стало)"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        'Success message has not disappeared'


