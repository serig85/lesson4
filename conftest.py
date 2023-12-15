import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")
