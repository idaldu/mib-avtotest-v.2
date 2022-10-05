from data.data import Person

class AuthLocators:
    ENTER_BUTTON = '//android.view.View[@content-desc="Войти"]'
    TELEPHONE_INPUT = '//android.widget.EditText[@index=3]'
    PASS_INPUT = '//android.widget.EditText[@index=5]'
    LOG_IN_BUTTON = "(//android.view.View[@content-desc=\"Войти\"])[2]"
    NUMBER_BUTTON_5 = '//android.view.View[@content-desc="0"]'
    SMS_TEXT = '//android.widget.TextView[contains(@text, "Внимание!")]'
    SMS_CONFIRM = '//android.view.View[@content-desc="Подтвердить"]'
    SMS_CONFIRM_BUTTON = '//android.view.View[@content-desc="СМС подтверждение"]'
    PUSH_CONFIRM_BUTTON = '(//android.view.View[@content-desc="Включить уведомления"])[2]'
    USER_NAME = f'//android.view.View[@content-desc="{Person.user_name}"]'
    # NOTIFICATION_BUTTON = 'open_notification_screen'