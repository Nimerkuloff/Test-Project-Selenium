import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_book_button_presents(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(4)

    element = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert len(element) != 0
