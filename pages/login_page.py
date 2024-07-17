from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_LOGIN_ALERT = (By.CSS_SELECTOR, '[data-test=error]')

    def __init__(self, driver): # It can be deleted because python checks for init driver in Basepage if it's not in  LoginPage
        super().__init__(driver)

    def login_user(self, username, password):
        self.find_element(self.USERNAME_FIELD).send_keys(username)
        self.find_element(self.PASSWORD_FIELD).send_keys(password)
        self.find_element(self.LOGIN_BUTTON).click()

    def get_invalid_login_error_message(self):
        return self.find_element(self.ERROR_LOGIN_ALERT).text