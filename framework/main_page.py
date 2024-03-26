from appium.webdriver.common.appiumby import AppiumBy

from framework.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def app_element(self, app_name: str):
        xpath = f'//android.widget.TextView[@content-desc="{app_name}"]'
        element = self.find_element(AppiumBy.XPATH, xpath)
        return element

    def start_app(self, app_name: str):
        app_element = self.app_element(app_name)
        app_element.click()

    def is_main_page(self):
        return bool(self.app_element('Chrome'))
