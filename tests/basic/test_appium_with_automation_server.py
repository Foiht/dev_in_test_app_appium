from appium.webdriver.common.appiumby import AppiumBy


def test_find_battery(driver) -> None:
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()
