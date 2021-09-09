# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:43:27 2021
Задание: оформляем тесты в стиле unittest 
Попробуйте оформить тесты из первого модуля в стиле unittest.

Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла 
Просмотрите отчёт о запуске и найдите последнюю строчку 
Отправьте эту строчку в качестве ответа на это задание 
Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения. 

Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке. 
@author: Tigrisha
"""
import unittest
from selenium import webdriver
import time

class TestRegistration(unittest.TestCase):
    def test_registration1(self, link="http://suninjuly.github.io/registration1.html"):
        browser = webdriver.Chrome()
        browser.get(link)
    
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input.first:required")
        input1.send_keys("Ivan")
        input3 = browser.find_element_by_css_selector("input.second:required")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_css_selector("input.third:required")
        input4.send_keys("Russia")
    
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Didn't get proper text")
    
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
        
    def test_registration2(self):
        self.test_registration1(link = "http://suninjuly.github.io/registration2.html")
        
if __name__ == "__main__":
    unittest.main()