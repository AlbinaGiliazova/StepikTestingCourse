#pytest -s test_product_page.py
# pytest -v --tb=line --language=en -m need_review

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time

#LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
LINK_PROMO = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


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
    

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK_PROMO)    
    page.open()                               
    page.should_get_add_to_basket_alert_text()              
    

@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='bug')) for i in range(10)])
def test_should_be_right_product_in_the_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)    
    page.open()                               
    page.should_be_right_product_in_the_basket()   
    

def test_should_be_right_price_in_the_basket(browser):
    page = ProductPage(browser, LINK_PROMO)    
    page.open()                               
    page.should_be_right_price_in_the_basket() 


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)  
    page.open() 
    page.add_product_to_basket()
    page.should_not_be_success_message() 
    
    
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)  
    page.open() 
    page.should_not_be_success_message()     
    
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)  
    page.open() 
    page.add_product_to_basket()
    page.should_disappear_success_message() 
   
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
    
@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    
    
def test_guest_can_see_empty_text_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_empty_text_present()
    
    
def test_guest_can_see_empty_text_in_basket_opened_from_product_page_en(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_empty_text_contains_en() 
    
@pytest.mark.need_review   
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_quantity_goods_not_present()     


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, login_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "strong123"
        page.register_new_user(email, password)
        
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK)  
        page.open() 
        page.should_not_be_success_message()      
       
    @pytest.mark.need_review    
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK)    
        page.open()                               
        page.add_product_to_basket()      
    
    
    
    
      