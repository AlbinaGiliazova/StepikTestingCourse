from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    
    def check_basket_empty_text_contains_en(self):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_LINK).text
        assert "Your basket is empty" in text, f"Got wrong basket text: {text}"     
    
    def check_basket_empty_text_present(self):
        assert  self.is_element_present(*BasketPageLocators.EMPTY_BASKET_LINK), "No empty basket text"
        
    def check_quantity_goods_not_present(self):
        assert  self.is_not_element_present(*BasketPageLocators.QUANTITY_GOODS_LINK), "There is a quantity of goods"        
        
     