from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocator:
    BUTTON_BASKET = (By.XPATH, "//div[@class ='basket-mini pull-right hidden-xs']//a[@class = 'btn btn-default']")
    BLOCK_BASKET_EMPTY = (By.XPATH, "//div[@id ='content_inner']/p")
    BLOCK_PRODUCTS_IN_THE_SHOPPING_CART = (By.XPATH, "//div[@class = 'basket-title hidden-xs']")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    INPUT_EMAIL = (By.XPATH, '//input[@id ="id_registration-email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id ="id_registration-password1"]')
    INPUT_REPEAT_PASSWORD = (By.XPATH, '//input[@id ="id_registration-password2"]')
    BUTTON_REGISTER = (By.XPATH, '//button[@name ="registration_submit"]')


class ProductPageLocators:
    BTN_ADD = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    MES_PROD_ADD = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]//strong")
    PRICE_NAME = (By.XPATH, "//div[contains(@class, 'col-sm-6 product_main')]/h1")
    PRICE_PRODUCT_MAIN = (By.XPATH, "//div[@class='col-sm-6 product_main']//p[@class='price_color']")
    COST_OF_THE_BASKET = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in'] //strong")
