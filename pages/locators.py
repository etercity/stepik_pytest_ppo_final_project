from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_IN_HEADER = (By.CSS_SELECTOR,".basket-mini > .btn-group > a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input#id_registration-email')
    PASS_FIELD =(By.CSS_SELECTOR, 'input#id_registration-password1')
    PASS_CONFIRM_FIELD = (By.CSS_SELECTOR, 'input#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')


class ProductPageLocators():
    # ADD_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_PRODUCT_NAME = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")
    SUM_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner > p > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div.alert-success')

    BTN_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    PROD_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong:nth-child(1)')
    PROD_NAME = (By.CSS_SELECTOR, '.product_main>h1')


class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items p.price_color")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@class='content']//p")


