#pytest -v --tb=line --language=en test_main_page.py
# pytest -s -v -m login_guest test_main_page.py

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

LINK = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser): 
        page = MainPage(browser, LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу         
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()    
      
        
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.should_be_login_link() 
        
        
    def test_guest_should_be_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()     
    
    
def test_guest_can_see_empty_text_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_empty_text_present()
    
    
def test_guest_can_see_empty_text_in_basket_opened_from_main_page_en(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_empty_text_contains_en() 
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_quantity_goods_not_present() 
    
    
    
