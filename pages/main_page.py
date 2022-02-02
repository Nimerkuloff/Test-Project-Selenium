from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage): 
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.login_link_locator), "Login link is not presented"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.login_link_locator)
        login_link.click()