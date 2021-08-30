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

    def should_be_add_to_basket(self):
        # проверка, что товар добавляется в корзину
        assert self.click_element(*ProductPageLocators.ADD_BTN), "Product don't add to basket"

    def should_be_add_correct_product(self):
        # проверка, что нужный товар добавлен в корзину
        assert self.get_text(*ProductPageLocators.PRODUCT_NAME).strip() == self.get_text(
            *ProductPageLocators.ADD_PRODUCT_NAME).strip(), "Product is not corrected"

    def should_be_correct_sum(self):
        # проверка, что сумма пересчиталась корректно
        assert self.get_num(*ProductPageLocators.SUM_BASKET) == self.get_num(
            *ProductPageLocators.PRODUCT_PRICE), "Sum is not corrected"



    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_BASKET)
        btn.click()

    def should_be_price_product_equal_real_product(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        print(price)
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        print(price_message)
        assert price == price_message, "Real price dosn't equal price in basket"

    def should_be_message_about_price_added_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE), \
            "Alert message about price doesn't exist"

    def should_be_message_about_product_added_basket(self):
        assert self.is_element_present(*ProductPageLocators.PROD_MESSAGE), \
            "Alert message about product isn't exist"

    def should_be_name_product_equal_real_product(self):
        prod_name = self.browser.find_element(*ProductPageLocators.PROD_NAME).text
        prod_message = self.browser.find_element(*ProductPageLocators.PROD_MESSAGE).text
        assert prod_name == prod_message, "Real prod name dosn't equal prod name in basket"
