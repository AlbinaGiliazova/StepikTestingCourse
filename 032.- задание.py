# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:25:58 2021
Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.
@author: Tigrisha
"""
from selenium import webdriver
import time 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_css_selector("[placeholder='Enter first name']")
    input1.send_keys("First name")
    
    input1 = browser.find_element_by_css_selector("[placeholder='Enter last name']")
    input1.send_keys("Last name")

    input1 = browser.find_element_by_css_selector("[placeholder='Enter email']")
    input1.send_keys("Email")    
    

    browser.find_element_by_id('file').send_keys(r"C:\Users\Tigrisha\Python_tasks\Stepik_AutoTestingPython\тексты\032.- задание.py")
    
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