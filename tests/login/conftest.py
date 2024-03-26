import pytest

from framework.navigator import Navigator


@pytest.fixture
def user_login_fixture(driver):
    yield Navigator(driver)
