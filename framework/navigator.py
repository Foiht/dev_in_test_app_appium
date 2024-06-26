import time

from appium.webdriver.webdriver import WebDriver

from framework.ajax.app_main_page import AppMainPage
from framework.ajax.login_page import LoginPage
from framework.ajax.root_page import RootPage
from framework.ajax.settings_page import SettingsPage


class Navigator:

    def __init__(self, driver: WebDriver):
        self.driver = driver

        self.root_page = RootPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.app_main_page = AppMainPage(self.driver)
        self.settings_page = SettingsPage(self.driver)

    def navigate_to_log_page(self) -> LoginPage:
        assert self.root_page.is_root_page()
        self.root_page.log_in().click()
        time.sleep(3)
        assert self.login_page.is_login_page()
        return self.login_page

    def navigate_to_main_page(self, user: str, password: str) -> AppMainPage:
        self.navigate_to_log_page()
        assert self.login_page.is_login_page()
        self.login_page.fill_user_credential(user, password)
        time.sleep(5)
        assert self.app_main_page.is_app_main_page()
        return self.app_main_page
