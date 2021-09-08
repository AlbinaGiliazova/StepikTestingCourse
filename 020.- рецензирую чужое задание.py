# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:22:11 2021

@author: Tigrisha
"""
from selenium import webdriver
import time


def offset10(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        first_name_field = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        first_name_field.send_keys('first_name')

        second_name_field = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        second_name_field.send_keys('second_name')

        email_field = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        email_field.send_keys('my_email')

        time.sleep(2)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(6)
        browser.quit()


if __name__ == '__main__':
    # offset10("http://suninjuly.github.io/registration1.html")
    offset10('http://suninjuly.github.io/registration1.html')