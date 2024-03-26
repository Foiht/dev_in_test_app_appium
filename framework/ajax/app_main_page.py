from appium.webdriver.webelement import WebElement

from framework.ajax.locators import MainPageLocators
from framework.base_page import BasePage


class AppMainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def menu_drawer(self) -> WebElement:
        return self.driver.find_element(*MainPageLocators.MENU_DRAWER)

    def app_setting(self) -> WebElement:
        self.menu_drawer().click()
        return self.driver.find_element(*MainPageLocators.APP_SETTINGS)

    def help(self) -> WebElement:
        self.menu_drawer().click()
        return self.driver.find_element(*MainPageLocators.HELP)

    def report(self) -> WebElement:
        self.menu_drawer().click()
        return self.driver.find_element(*MainPageLocators.REPORT_PROBLEM)

    def add_space(self) -> WebElement:
        self.menu_drawer().click()
        return self.driver.find_element(*MainPageLocators.ADD_SPACE)

    def is_app_main_page(self) -> bool:
        return bool(self.menu_drawer())
