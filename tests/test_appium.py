import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

desired_capabilities = UiAutomator2Options().load_capabilities(capabilities)


@pytest.fixture
def driver_base():
    driver = webdriver.Remote('http://localhost:4723', options=desired_capabilities)
    yield driver
    if driver:
        driver.quit()


def test_find_battery(driver_base) -> None:
    el = driver_base.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()
