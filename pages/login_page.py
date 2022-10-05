from pytest_bdd import scenario, given, when, then
from locators.login_page_locators import AuthLocators
from data.data import Person
from pages.base_page import BasePage
import allure


class AuthPage(BasePage):
    locators = AuthLocators()

    @allure.step('Заполнение полей (ДН, пароль)')
    def fill_all_fields(self):
        with allure.step('заполнение полей'):
            self.click(self.locators.ENTER_BUTTON)
            self.input(Person.trusted_number, self.locators.TELEPHONE_INPUT)
            self.input(Person.password, self.locators.PASS_INPUT)
        with allure.step('сворачивание клавиатуры'):
            self.driver.hide_keyboard()
        with allure.step('нажатие кнопки подтверждения'):
            self.click(self.locators.LOG_IN_BUTTON)

    @allure.step('Ввод кода доступа и подтверждение его')
    def input_acesscode(self):
        for j in range(2):
            for i in range(4):
                self.click(self.locators.NUMBER_BUTTON_5)

    @allure.step('Ввод кода OTP c СМС')
    def input_smscode(self):
        if Person.app_type == 'test':
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

    @allure.step('Выбор второго фактора авторизации - СМС')
    def sms_confirm(self):
        self.click(self.locators.SMS_CONFIRM_BUTTON)
    
    @allure.step('Согласие на получение push-уведомлений')
    def push_confirm(self):
        self.click(self.locators.PUSH_CONFIRM_BUTTON)

    @allure.step('Переход в личный кабинет, проверка авторизации')
    def click_user_name(self):
        self.click(self.locators.USER_NAME)

    # def click_notifications(self):
    #     self.click_flutter(self.locators.NOTIFICATION_BUTTON)