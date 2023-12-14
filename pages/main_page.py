from .base_page import BasePage
from .basket_page import BasketPage
from selenium.webdriver.common.by import By
from .login_page import LoginPage
from .locators import MainPageLocators

class MainPage(BasePage, BasketPage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)



    def add_to_basket(self):
        add =self.browser.find_element(By.XPATH, "//*[@id='default']/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/form/button")
        add.click()





