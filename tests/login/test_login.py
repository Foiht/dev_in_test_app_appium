import logging
import time

import pytest
import allure

from config import user_mail, user_password

params_invalid = (
    ("username", "password", "Invalid email format"),
    (1234, 7657, 'Invalid email format'),
    ("aa@gmail.com", "***", "Wrong login or password")
)

params_valid = (
    (user_mail, user_password),
)


@allure.feature('Login Page Test')
class TestLoginPage:

    @pytest.fixture(autouse=True, scope="function")
    def setup_teardown(self, user_login_fixture):
        self.navigator = user_login_fixture

        self.login_page = self.navigator.navigate_to_log_page()

        yield

    def test_element_login_page_email(self):
        with allure.step("Testing user login page element: Email text field"):
            element_email = self.login_page.user_field()
            assert element_email, f"Element email is not found"
            assert element_email.is_enabled(), f"Element email is disabled"
            logging.info(fr"Element email is verified, {element_email.text}")

    @pytest.mark.parametrize('login, password, msg', params_invalid)
    def test_user_log_in_invalid(self, login, password, msg):
        with allure.step("Testing user login page: invalid login"):
            self.login_page.fill_user_credential(login, password)
            popup_message = self.login_page.invalid_message()
            assert popup_message, f"Popup message is not found"
            assert popup_message.text.startswith(msg)
            logging.info(f"Negative test is PASSED, Message: {popup_message.text}")

    @pytest.mark.parametrize('login, password', params_valid)
    def test_user_log_in_valid(self, login, password):
        with allure.step("Testing user login page: valid login"):
            self.login_page.fill_user_credential(login, password)
            time.sleep(5)
            assert self.navigator.app_main_page.is_app_main_page(), "Unexpected behavior, AppMainPage was not found"
