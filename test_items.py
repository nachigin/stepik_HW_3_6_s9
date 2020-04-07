#3_6 step 9
import time

def test_guest_should_see_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(3)

    but1 = browser.find_elements_by_css_selector('button.btn-add-to-basket')
    #but1.click()
    time.sleep(3)
    # browser.find_elements_by_css_selector('button.btn-add-to-basket')
    # browser.find_element_by_id("add_to_basket_form")
    assert but1, 'Кнопка отсутствует'