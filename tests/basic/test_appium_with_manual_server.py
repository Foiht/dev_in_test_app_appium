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


@pytest.mark.skip(reason="'Test should be run separately from others")
def test_find_homepage_title(driver_base) -> None:
    """
    Test established connection with Appium server and Android emulator
    Run Appium server with default settings:
    $ appium
    """
    el = driver_base.find_element(by=AppiumBy.ID, value='com.android.settings:id/homepage_title')
    el.is_enabled()
