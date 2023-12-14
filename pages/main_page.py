from .base_page import BasePage
from selenium.webdriver.common.by import By
from .login_page import LoginPage
from .locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def click_to_basket(self):
        btn_add = self.browser.find_element(*MainPageLocators.BUTTON_BASKET)
        btn_add.click()

    def add_to_basket(self):
        add =self.browser.find_element(By.XPATH, "//*[@id='default']/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/form/button")
        add.click()

    def should_be_basket_clear(self):
        self.should_block_basket_empty()
        self.should_not_be_block_products_in_the_shopping_cart()

    def should_not_be_block_products_in_the_shopping_cart(self):
        assert self.is_not_element_present(*MainPageLocators.BLOCK_PRODUCTS_IN_THE_SHOPPING_CART), \
           "Success message is presented, but should not be"
    def should_block_basket_empty(self):
        assert self.is_element_present(*MainPageLocators.BLOCK_BASKET_EMPTY)
