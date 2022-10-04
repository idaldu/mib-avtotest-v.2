from pytest_bdd import scenario, given, when, then
from locators.login_page_locators import AuthLocators
from pages.base_page import BasePage
import conftest


class AuthPage(BasePage):
    locators = AuthLocators()

    @scenario('elements_test.feature', 'Авторизация')
    def test_publish(self):
        pass

    @when('Tap on login button')
    def click_button_enter(self):
        self.click(self.locators.ENTER_BUTTON)

    @given('Ввести 008131393 в поле телефона')
    def input_number(self, text):
        self.input(text, self.locators.TELEPHONE_INPUT)

    @when('Ввести Colvir456! в поле пароля')
    def input_password(self, text):
        self.input(text, self.locators.PASS_INPUT)

    @when('Нажать кнопку Войти')
    def tap_login(self):
        self.click(self.locators.LOG_IN_BUTTON)

    def click_button_log_in(self):
        self.click(self.locators.LOG_IN_BUTTON)

    @when('Ввести код доступа')
    def input_acesscode(self):
        for j in range(2):
            for i in range(4):
                self.click(self.locators.NUMBER_BUTTON_5)

    @when('Ввести код из смс')
    def input_smscode(self):
        if conftest.type_app == 'test':
            code = "111111"
        else:
            # Код из смс сообщения
            while not self.driver.is_keyboard_shown():
                print("waiting")
            self.driver.open_notifications()
            tryes = 0

            while True:
                try:
                    # self.find_element(By.ID, 'android:id/message_text')
                    self.find_element(self.locators.SMS_TEXT)
                    break
                except:
                    tryes += 1
                    print("wait for sms...")
                    if tryes > 5:
                        break

            # sms = self.find_element(By.ID, 'android:id/message_text').text
            sms = self.find_element(self.locators.SMS_TEXT).text
            print(sms)
            code = sms.split()[0]
            print(code)
            self.driver.back()

        self.input_keycode(code)
        self.driver.hide_keyboard()
        self.click(self.locators.SMS_CONFIRM)

    @when('Выбрать смс подтверждение')
    def tap_sms_confirm(self):
        self.click(self.locators.SMS_CONFIRM_BUTTON)
