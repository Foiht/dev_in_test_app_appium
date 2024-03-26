import pytest

from config import user_mail, user_password
from framework.navigator import Navigator


@pytest.fixture(scope="module")
def main_page_fixture(driver_module):
    navigator = Navigator(driver_module)
    main_page = navigator.navigate_to_main_page(user_mail, user_password)
    yield main_page
