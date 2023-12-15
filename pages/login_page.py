from time import sleep
from .locators import LoginPageLocators
from .locators import BasePageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        sleep(5)
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        form1 = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        form1.send_keys(email)
        form2 = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        form2.send_keys(password)
        form3 = self.browser.find_element(*LoginPageLocators.INPUT_REPEAT_PASSWORD)
        form3.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button.click()
        sleep(6)
        assert self.is_element_present(*BasePageLocators.USER_ICON)
