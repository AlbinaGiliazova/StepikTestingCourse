# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:00:52 2021

@author: Tigrisha
"""
from selenium import webdriver
import time 

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    fn = browser.find_element_by_tag_name('input')
    fn.send_keys('Ivan')
    
    ln = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    ln.send_keys('Zaycev')

    mail = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    mail.send_keys('rtyrtyr@mail.ru')
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()