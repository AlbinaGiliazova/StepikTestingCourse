# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 17:22:07 2021
Задание: параметризация тестов
Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим сценарием действий: 

открыть страницу 
ввести правильный ответ 
нажать кнопку "Отправить" 
дождаться фидбека о том, что ответ правильный 
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
Опциональный фидбек — это текст в черном поле, как показано на скриншоте: 



Правильным ответом на задачу в заданных шагах является число:

import time
import math

answer = math.log(int(time.time()))
Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров: 

https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1

Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания, чтобы тесты работали стабильно. 

В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает со строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание. 

Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено правильное локальное время (https://time.is/ru/). Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают. 
@author: gilia
"""

import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    input1 = browser.find_element_by_css_selector("textarea")
    input1.send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_class_name("submit-submission").click()
    #time.sleep(30)
    res = browser.find_element_by_class_name("smart-hints__hint")
    assert res.text == "Correct!", f"{res.text}"