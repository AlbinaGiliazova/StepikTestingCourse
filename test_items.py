import time

def test_should_see_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    #time.sleep(30)
    button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert button > 0, '!!!НЕ НАШЕЛ!!!'