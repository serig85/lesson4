from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    BTN_ADD=(By.CLASS_NAME,"btn.btn-lg.btn-primary.btn-add-to-basket")
    MES_PROD_ADD=(By.XPATH,"//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]//strong")
    PRICE_NAME=(By.XPATH,"//div[contains(@class, 'col-sm-6 product_main')]/h1")
    PRICE_PRODUCT_MAIN=(By.XPATH,"//div[@class='col-sm-6 product_main']//p[@class='price_color']")
    COST_OF_THE_BASKET= (By.XPATH,"//div[@class='alert alert-safe alert-noicon alert-info  fade in'] //strong")

