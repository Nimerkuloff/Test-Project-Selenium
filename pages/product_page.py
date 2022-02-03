from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    #to brake arrange and assess parts, how to access before_click values after browser change?
    def add_to_basket_AND_should_add_to_basket(self):

        add_to_basket_button = self.browser.find_element(*ProductPageLocators.product_add_to_basket_button)

        before_click_price = self.browser.find_element(*ProductPageLocators.product_price).text
        before_click_name = self.browser.find_element(*ProductPageLocators.product_name).text

        add_to_basket_button.click()

        basket_total = self.browser.find_element(*ProductPageLocators.product_basket_total).text
        result_text = self.browser.find_element(*ProductPageLocators.add_alertinner).text

        assert before_click_price == basket_total, "==== PRICE AND BASKET TOTAL MISMATCH ===="
        assert before_click_name == result_text, "==== NAMES AFTER AND BEFORE ADDING TO BASKET MISMATCH ===="

        print("PRODUCT ADDED: " + result_text.replace(" has been added to your basket." , " "))
        print(basket_total)


