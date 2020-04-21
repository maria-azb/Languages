import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"	

def test_button(browser):
    browser.get(link)
    time.sleep(10)
    browser.find_element_by_css_selector(".btn-add-to-basket")
    assert True, "Some Error"
	