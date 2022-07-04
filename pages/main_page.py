from .locators import LoginPageLocators
from .locators import BasePageLocators
from .base_page import BasePage



class MainPage(BasePage):
    def go_to_login_page(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

