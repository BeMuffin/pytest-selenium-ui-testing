import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login_user(browser):
    login_page = LoginPage(browser)
    login_page.open_url()    
    login_page.login_user('standard_user','secret_sauce')
    current_url = login_page.get_current_url()
    assert 'inventory.html' in current_url
    yield



