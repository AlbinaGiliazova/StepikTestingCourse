#pytest -s test_product_page.py

from pages.product_page import ProductPage
import pytest

#LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#LINK = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# def test_should_be_add_to_basket_button(browser):
#     page = ProductPage(browser, LINK)
#     page.open()
#     page.should_be_add_to_basket_button() 
    
    
# def test_should_be_product_name(browser):
#     page = ProductPage(browser, LINK)
#     page.open()
#     page.should_be_product_name()     
    
    
# def test_should_be_product_price(browser):
#     page = ProductPage(browser, LINK)
#     page.open()
#     page.should_be_product_price()        
    


# def test_guest_can_add_product_to_basket(browser):
#     page = ProductPage(browser, LINK)    
#     page.open()                               
#     page.should_get_add_to_basket_alert_text()              
    

# @pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='bug')) for i in range(10)])
# def test_should_be_right_product_in_the_basket(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#     page = ProductPage(browser, link)    
#     page.open()                               
#     page.should_be_right_product_in_the_basket()   
    

# def test_should_be_right_price_in_the_basket(browser):
#     page = ProductPage(browser, LINK)    
#     page.open()                               
#     page.should_be_right_price_in_the_basket() 


# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, LINK)  
#     page.open() 
#     page.add_product_to_basket()
#     page.should_not_be_success_message() 
    
    
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, LINK)  
#     page.open() 
#     page.should_not_be_success_message()     
    
    
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, LINK)  
#     page.open() 
#     page.add_product_to_basket()
#     page.should_disappear_success_message() 
   
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
       
    
    
    
    
    
      