# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:07:40 2021

@author: Tigrisha
"""
from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x1_element = browser.find_element_by_id('num1')
    x1 = x1_element.text
    x2_element = browser.find_element_by_id('num2')
    x2 = x2_element.text    
    y = str(int(x1) + int(x2))
    
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(y)
    
    button = browser.find_element_by_xpath('.//button[text()="Submit"]')
    button.click()    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
# Системы UNIX/Linux ожидают пустую строку в конце файла, если в вашем скрипте 
# ее не будет, то последняя строчка, содержащая код, может не выполниться.