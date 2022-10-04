import time

from pages.login_page import AuthPage


class TestElement:
    class TestLogin:

        def test_enter_box(self, driver):
            test_enter_box = AuthPage(driver)


            test_enter_box.click_button_enter()
            test_enter_box.input_number('557227828')
            test_enter_box.input_password('Colvir1234**')
            driver.hide_keyboard()
            test_enter_box.click_button_log_in()
            test_enter_box.input_acesscode()
            test_enter_box.input_smscode()
            test_enter_box.tap_sms_confirm()
            time.sleep(5)