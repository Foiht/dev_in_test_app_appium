from framework.ajax.locators import LoginPageLocators
from framework.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_user_credential(self, username: str, password: str) -> None:
        element_email = self.find_element(*LoginPageLocators.EMAIL_FIELD)
        element_email.send_keys(username)

        element_password = self.find_element(*LoginPageLocators.PASSWORD_FIELD)
        element_password.send_keys(password)

    def click_login_button(self) -> None:
        element = self.find_element(*LoginPageLocators.AUTOLOGIN_BUTTON)
        element.click()
