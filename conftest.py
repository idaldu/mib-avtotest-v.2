import pytest
from appium import webdriver

# prod or test
type_app = 'test'


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "Redmi",
            "app": f"C:\\Users\\adubov\\PycharmProjects\\mib-avtotest-v.2\\app_binaries\\mib-{type_app}.apk"
        })
    driver.implicitly_wait(10)
    yield driver  # Test code runs after this line

    # Teardown
    driver.quit()
