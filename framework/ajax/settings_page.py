from appium.webdriver.webelement import WebElement

from framework.ajax.locators import SettingsPageLocators
from framework.base_page import BasePage


class SettingsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def sign_out(self) -> WebElement:
        return self.driver.find_element(*SettingsPageLocators.LOG_OUT)

    def is_setting_page(self) -> bool:
        return bool(self.sign_out())
