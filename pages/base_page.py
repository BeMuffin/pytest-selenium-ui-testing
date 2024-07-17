from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url= 'https://www.saucedemo.com/'
    
    def open_url(self):
        return self.driver.get(self.base_url)
    
    def find_element(self,locator, time =10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),message=f"Can't find element {locator}")

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def get_current_url(self):
        return self.driver.current_url
    
    def get_title(self):
        return self.driver.title