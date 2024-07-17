from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    ADD_TO_CART_BACKPACK_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_TO_CART_BIKE_LIGHT_BUTTON = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')

    def add_item_to_cart(self,itemName):
        itemsDict = self.create_items_dict()
        itemLocator = itemsDict.get(itemName)
        self.find_element(itemLocator).click()

    def create_items_dict (self):
        product_items = {
            'backpack': self.ADD_TO_CART_BACKPACK_BUTTON,
            'bike light': self.ADD_TO_CART_BIKE_LIGHT_BUTTON
        }
        return product_items

    def get_cart_badge_text(self):
        return self.find_element(self.CART_BADGE).text
    
    def is_cart_badge_displayed(self):
        return self.find_element(self.CART_BADGE).is_displayed()
