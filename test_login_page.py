from time import sleep
from .pages.login_page import LoginPage


def test_guest_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    sleep(5)
    LoginPage.should_be_login_page(page)
