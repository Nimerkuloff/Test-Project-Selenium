from selenium.webdriver.common.by import By


class MainPageLocators():
    login_link_locator = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form_locator = (By.CSS_SELECTOR, "form#login_form")
    reg_form_locator = (By.CSS_SELECTOR, "form#register_form")

class ProductPageLocators():
    product_add_to_basket_button = (By.CSS_SELECTOR, ".btn-add-to-basket")
    add_alertinner = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong")
    product_basket_total = (By.CSS_SELECTOR, ".alert:nth-last-child(1) strong")
    product_price = (By.CSS_SELECTOR, "div.col-sm-6.product_main .price_color")
    product_name = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")