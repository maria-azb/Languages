import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket_present(browser):
    browser.get(link)
    time.sleep(10)
    try:	
        browser.find_element_by_css_selector(".btn-add-to-basket")
        is_button = True
    except (NoSuchElementException):
        is_button = False    	
    assert is_button == True, "Button 'add to basket' wasn't found"
	