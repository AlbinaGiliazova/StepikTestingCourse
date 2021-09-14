#pytest -s test_product_page.py

from pages.product_page import ProductPage
import pytest

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_should_be_add_to_basket_button(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_add_to_basket_button() 
    
    
def test_should_be_product_name(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_product_name()     
    
    
def test_should_be_product_price(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_product_price()        
    


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK)    
    page.open()                               
    page.should_get_add_to_basket_alert_text()              
    

@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='bug')) for i in range(10)])
def test_should_be_right_product_in_the_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)    
    page.open()                               
    page.should_be_right_product_in_the_basket()   
    

def test_should_be_right_price_in_the_basket(browser):
    page = ProductPage(browser, LINK)    
    page.open()                               
    page.should_be_right_price_in_the_basket()       