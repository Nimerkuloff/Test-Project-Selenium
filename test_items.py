import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_book_button_presents(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(30)

    element = WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="btn-add-to-basket"]'))
    )

    assert element.text != ""
