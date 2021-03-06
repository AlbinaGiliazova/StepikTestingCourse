# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 11:58:45 2021
Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

 

Когда ваш код заработает, попробуйте запустить его на странице http://suninjuly.github.io/selects2.html. Ваш код и для нее тоже ﻿должен пройти успешно.

Подсказка: если вы получаете ошибку в духе "argument of type 'int' is not iterable", перепроверьте тип переменной, которую вы передаете в функцию поиска. Нужно передать строку! 
@author: Tigrisha
"""
from selenium import webdriver
import time 

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x1_element = browser.find_element_by_id('num1')
    x1 = x1_element.text
    x2_element = browser.find_element_by_id('num2')
    x2 = x2_element.text    
    y = str(int(x1) + int(x2))
    
    browser.find_element_by_id('dropdown').click()
    browser.find_element_by_css_selector(f"[value='{y}']").click()     
    
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