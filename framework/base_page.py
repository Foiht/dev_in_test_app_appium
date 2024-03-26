import logging

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_cond


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_until_element_present(self, locator_data, timeout=5) -> WebElement:
        waiter = WebDriverWait(self.driver, timeout)
        element = waiter.until(exp_cond.presence_of_element_located(locator_data))
        return element

    def find_element(self, locator_type, locator) -> WebElement:
        try:
            element = self.driver.find_element(locator_type, locator)
            return element
        except NoSuchElementException:
            logging.debug(f"Element not found without waiting, {locator_type, locator}")
        return self.wait_until_element_present((locator_type, locator))

    def go_back(self):
        self.driver.back()

    @staticmethod
    def click_element(element_obj: WebElement) -> None:
        element_obj.click()

    @staticmethod
    def fill_text_field(field_elem: WebElement, keys: str) -> None:
        field_elem.send_keys(keys)
