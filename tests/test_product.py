import pytest
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage

@pytest.mark.usefixtures('login_user')
def test_add_product_item_to_cart(browser):
    product_page = ProductPage(browser)
    product_page.add_item_to_cart('backpack')
    assert product_page.is_cart_badge_displayed() is True
    assert '1' in product_page.get_cart_badge_text()
