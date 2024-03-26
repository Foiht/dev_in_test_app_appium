import pytest

from framework.navigator import Navigator


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield Navigator(driver)
