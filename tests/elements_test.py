import time

from pages.login_page import AuthPage


class TestElement:
    class TestEnterBox:

        def test_enter_box(self, driver):
            test_enter_box = AuthPage(driver)

            test_enter_box.click_button_enter()