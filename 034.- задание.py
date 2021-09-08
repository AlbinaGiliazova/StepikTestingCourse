# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:38:15 2021
Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.
@author: Tigrisha
"""
from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_xpath('.//button[text()="I want to go on a magical journey!"]')
    button.click()   

    alert = browser.switch_to.alert
    alert.accept()        
    
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

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