from appium.webdriver import WebElement

from framework.ajax.locators import RootPageLocators
from framework.base_page import BasePage


class RootPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def log_in(self) -> WebElement:
        return self.find_element(*RootPageLocators.LOGIN_BUTTON)

    def create_account(self) -> WebElement:
        return self.find_element(*RootPageLocators.CREATE_ACCOUNT_BUTTON)

    def is_root_page(self):
        return bool(self.log_in())
