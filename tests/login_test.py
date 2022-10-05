import time
import allure
from pages.login_page import AuthPage

@allure.suite('Авторизация, выход из сессии')
class TestAuthorization:
    
    @allure.feature('Авторизация')
    class TestLogin:

        @allure.title('Проверка авторизации пользователя')
        def test_login(self, driver):
            test_login = AuthPage(driver)
            
            test_login.fill_all_fields()
            test_login.input_acesscode()
            test_login.input_smscode()
            test_login.sms_confirm()
            test_login.push_confirm()
            test_login.click_user_name()
            # test_login.click_notifications()
            time.sleep(5)