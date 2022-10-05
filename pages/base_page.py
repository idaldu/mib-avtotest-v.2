from selenium.webdriver.common.by import By
# from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def click(self, locator):
        e = self.find_element(locator)
        e.click()

    def input(self, text, locator):
        el = self.find_element(locator)
        el.clear()
        el.click()
        print(text)
        el.send_keys(text)

    def input_keycode(self, text):
        arr = list(text)
        for i in arr:
            self.driver.press_keycode(7 + int(i))

    def swipe_to_refresh(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(500, 400)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(500, 1300)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def output(self, locator):
        el = self.find_element(locator).text
        return el

    # def click_flutter(self, locator):
    #     finder = FlutterFinder()
    #     key_finder = finder.by_value_key(locator)
    #     el = FlutterElement(driver, key_finder)
    #     el.click()

   # def wait(self, time):
   #     self.driver.implicitly_wait(time)