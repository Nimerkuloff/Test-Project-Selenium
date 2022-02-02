from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "==== NOT A LOGIN URL ===="

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form_locator), "==== NOT A LOGIN FORM ===="

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.reg_form_locator), "==== NOT A REGISTER FORM ===="