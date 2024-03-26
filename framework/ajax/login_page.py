from appium.webdriver import WebElement

from framework.ajax.locators import LoginPageLocators
from framework.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def user_field(self) -> WebElement:
        return self.find_element(*LoginPageLocators.EMAIL_FIELD)

    def password_field(self) -> WebElement:
        return self.find_element(*LoginPageLocators.PASSWORD_FIELD)

    def login_button(self) -> WebElement:
        return self.find_element(*LoginPageLocators.AUTOLOGIN_BUTTON)

    def fill_user_credential(self, username: str, password: str) -> None:
        self.user_field().send_keys(username)
        self.password_field().send_keys(password)
        self.login_button().click()

    def is_login_page(self) -> bool:
        return bool(self.find_element(*LoginPageLocators.EMAIL_FIELD))

