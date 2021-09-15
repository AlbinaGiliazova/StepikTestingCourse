from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")  
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    

class BasketPageLocators():
    EMPTY_BASKET_LINK = (By.CSS_SELECTOR, "#content_inner p")    
    QUANTITY_GOODS_LINK = (By.CSS_SELECTOR, "#id_form-0-quantity")    


class LoginPageLocators: 
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    

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
                    
    
 

    