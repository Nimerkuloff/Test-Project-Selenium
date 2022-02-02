from selenium.webdriver.common.by import By


class MainPageLocators():
    login_link_locator = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form_locator = (By.CSS_SELECTOR, "form#login_form")
    reg_form_locator = (By.CSS_SELECTOR, "form#register_form")