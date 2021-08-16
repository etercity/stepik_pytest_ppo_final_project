from .base_page import BasePage
from .locators import  BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        """ Проверяеет, что в корзине нет товаров """
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
        'Basket is not empty!'

    def should_be_empty_basket_message(self):
        """ Проверяет, что есть сообщение о пустой корзине """
        empty_basket_message =''
        if self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE) == True:
            empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert 'Your basket is empty. Continue shopping' == empty_basket_message.strip(), 'Empty basket message is not presented!'


