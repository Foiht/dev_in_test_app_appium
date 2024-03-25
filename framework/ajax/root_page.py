from framework.ajax.locators import RootPageLocators
from framework.base_page import BasePage


class RootPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def log_in_page_click(self) -> None:
        login_element = self.find_element(*RootPageLocators.LOGIN_BUTTON)
        login_element.click()

    def create_account_page_click(self) -> None:
        login_element = self.find_element(*RootPageLocators.CREATE_ACCOUNT_BUTTON)
        login_element.click()
