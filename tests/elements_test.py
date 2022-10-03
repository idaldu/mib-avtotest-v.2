from selenium.webdriver.common.by import By

from pages.base_page import BasePage


def test_basic(driver):
    WAIT_SEC = 10
    driver.implicitly_wait(WAIT_SEC)
    base = BasePage(driver)
    element = (By.XPATH, '//android.view.View[@content-desc="Войти"]')
    base.click(element)

# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage
#
#
# class ElementsTest(BasePage):
#     def test(self):
#         element = (By.XPATH, '//android.view.View[@content-desc="Войти"]')
#         self.click(self, element)