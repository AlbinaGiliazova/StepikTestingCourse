from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    

class MainPageLocators:
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    pass
    
    
class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_PRODUCT =  (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner > strong") 
    ADDED_PRICE =  (By.CSS_SELECTOR, ".alertinner >p >strong")     
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1") 
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color") 
    SUCCESS_MESSAGE =   (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner")   
                    
    
 

    