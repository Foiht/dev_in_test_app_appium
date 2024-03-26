import logging

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_cond


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_until_element_present(self, locator_data, timeout=5) -> WebElement | bool:
        try:
            waiter = WebDriverWait(self.driver, timeout)
            element = waiter.until(exp_cond.presence_of_element_located(locator_data))
            logging.info(f'Element was found with {timeout=}, "{locator_data}"')
            return element
        except TimeoutException:
            logging.info(f'Element was not found after {timeout=}, "{locator_data}"')
            return False

    def find_element(self, locator_type, locator) -> WebElement | bool:
        try:
            element = self.driver.find_element(locator_type, locator)
            logging.info(f'Element was found, "{locator_type, locator}"')
            return element
        except NoSuchElementException:
            return self.wait_until_element_present((locator_type, locator))

    def go_back(self):
        self.driver.back()
