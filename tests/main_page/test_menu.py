import logging

import pytest
import allure


@allure.feature('Main Page Test')
class TestMenuPage:

    @pytest.fixture(autouse=True)
    def setup_teardown(self, main_page_fixture):
        self.main_page = main_page_fixture

        yield

    def test_element_main_page_menu_app_settings(self):
        with allure.step("Testing main page menu element: App settings button"):
            elem = self.main_page.app_setting()
            assert elem, f"Element App settings is not found"
            assert elem.is_enabled(), f"Element App settings is disabled"
            logging.info(f"Element App settings is verified")

    def test_element_main_page_menu_help(self):
        with allure.step("Testing main page menu element: Help button"):
            elem = self.main_page.help()
            assert elem, f"Element Help is not found"
            assert elem.is_enabled(), f"Element Help is disabled"
            logging.info(f"Element Help is verified")

    def test_element_main_page_menu_report(self):
        with allure.step("Testing main page menu element: Report Problem button"):
            elem = self.main_page.report()
            assert elem, f"Element Report problem is not found"
            assert elem.is_enabled(), f"Element Report problem is disabled"
            logging.info(f"Element Report problem is verified")

    def test_element_main_page_menu_add_space(self):
        with allure.step("Testing main page menu element: Add space button"):
            elem = self.main_page.add_space()
            assert elem, f"Element Add space is not found"
            assert elem.is_enabled(), f"Element Add space is disabled"
            logging.info(f"Element Add space is verified")

    def test_element_main_page_menu_terms_of_service(self):
        with allure.step("Testing main page menu element: Terms of service button"):
            elem = self.main_page.terms_of_service()
            assert elem, f"Element Terms of service is not found"
            assert elem.is_enabled(), f"Element Terms of service is disabled"
            logging.info(f"Element Terms of service is verified")
