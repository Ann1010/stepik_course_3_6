import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

def test_check_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    time.sleep(30)
    assert button != None, "Кнопка отсутствует"
