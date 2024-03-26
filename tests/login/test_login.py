import logging
import time

import pytest
import allure

from config import user_mail, user_password

params = (
    ("username", "password", False),
    (1234, 7657, False),
    (user_mail, user_password, True)
)


@allure.feature('Random dog')
class TestLoginPage:

    @pytest.fixture(autouse=True, scope="function")
    def setup_teardown(self, user_login_fixture):
        self.navigator = user_login_fixture

        self.login_page = self.navigator.navigate_to_log_page()

        yield

    def test_element_login_page_email(self):
        with allure.step("Testing user login page element: Email text field"):
            element_email = self.login_page.user_field()
            logging.info(f'{dir(element_email)}')
            assert element_email, f"Element email is not found"
            assert element_email.is_enabled(), f"Element email is disabled"

    @pytest.mark.parametrize('login, password, success', params)
    def test_user_log_in(self, login, password, success):
        with allure.step("Testing user login page: login scenario"):
            self.login_page.fill_user_credential(login, password)
            time.sleep(3)
            assert self.navigator.app_main_page.is_app_main_page() == success, (f"Unexpected result, "
                                                                                f"check for App Main Page "
                                                                                f"should be {success}")

