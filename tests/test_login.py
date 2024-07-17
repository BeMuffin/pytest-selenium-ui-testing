from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_login_valid_user(browser):
    login_page = LoginPage(browser)
    login_page.open_url()
    assert 'Swag Labs' in login_page.get_title()
    
    login_page.login_user('standard_user','secret_sauce')
    assert login_page.get_current_url() == 'https://www.saucedemo.com/inventory.html'

def test_login_invalid_user(browser):
    login_page = LoginPage(browser)
    login_page.open_url()
    assert 'Swag Labs' in login_page.get_title()

    login_page.login_user('locked_out_user','secret_sauce')
    assert login_page.get_invalid_login_error_message() == 'Epic sadface: Sorry, this user has been locked out.'