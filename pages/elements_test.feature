Feature: Test for log in

  Background:
    When Tap on login button

  Scenario: Авторизация
    Given Ввести 008131393 в поле телефона
    When Ввести Colvir456! в поле пароля
    When Нажать кнопку Войти
    When Ввести код доступа
    When Ввести код из смс
    When Выбрать смс подтверждение
