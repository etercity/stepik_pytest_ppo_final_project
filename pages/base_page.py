from selenium.common.exceptions import *
from selenium.common.exceptions import NoAlertPresentException
import math
from .locators import  BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class BasePage():
    """ Класс базовой страницы """
    def __init__(self, browser, url, timeout=10):
        """ Конструктор, вызывающий браузер """
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        """ Переходит на страницу логина """
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_basket_in_header(self):
        """ Переходит в корзину по кнопке из шапки """
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_IN_HEADER)
        basket_button.click()


    def is_element_present(self, how, what):
        """ """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """ Проверяет, что элемент не появился в течение timeout """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """ Проверяет, что элемент исчезает со страницы в течение timeout """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):
        """ Открывает страницу в браузере """
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_login_link(self):
        """ Находит ссылку на страницу логина  """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        """ Проверяет, что пользователь залогинен """
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def click_element(self, how, what):
        try:
            self.browser.find_element(how, what).click()
        except NoSuchElementException:
            return False
        return True

    def get_text(self, how, what):
        try:
            return self.browser.find_element(how, what).text
        except NoSuchElementException:
            return None

    def get_num(self, how, what):
        try:
            numtxt = self.browser.find_element(how, what).text.replace(',', '.')
            return float(re.findall(r'\d+.\d+', numtxt)[0])
        except NoSuchElementException:
            return None

