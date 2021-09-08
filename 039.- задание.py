# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:14:25 2021
Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.
@author: Tigrisha
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )
    browser.find_element_by_id("book").click()
    
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