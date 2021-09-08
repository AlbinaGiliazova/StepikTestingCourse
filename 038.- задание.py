# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:07:01 2021
Какую ошибку вы увидите в консоли, если попытаетесь выполнить команду browser.find_element_by_id("button") после открытия страницы http://suninjuly.github.io/cats.html?
@author: Tigrisha
"""
from selenium import webdriver
import time 

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_id("button") 

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
# Системы UNIX/Linux ожидают пустую строку в конце файла, если в вашем скрипте 
# ее не будет, то последняя строчка, содержащая код, может не выполниться.