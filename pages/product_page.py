from .base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
        
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"  
        
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"         

    def should_get_add_to_basket_alert_text(self):
        self.add_product_to_basket()       
        assert self.solve_quiz_and_get_code(), "Didn't get the alert text"
        
    def should_be_right_product_in_the_basket(self):
        self.add_product_to_basket()        
        self.solve_quiz_and_get_code()
        text = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT).text
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == text, f"Not the right product in the basket: {text}" 
        
    def should_be_right_price_in_the_basket(self):
        self.add_product_to_basket()        
        self.solve_quiz_and_get_code()
        text = self.browser.find_element(*ProductPageLocators.ADDED_PRICE).text
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in text, "Not the right price in the basket"  
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"    
           
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message didn't disappear', but should"            
        
        