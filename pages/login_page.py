from locators.elements_page_locators import AuthLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    locators = AuthLocators()

    def click_button_enter(self):
        self.click(self.locators.ENTER_BUTTON)
