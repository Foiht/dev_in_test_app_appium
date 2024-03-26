import time

from framework.ajax.root_page import RootPage


def test_app_ajax(driver) -> None:
    time.sleep(10)
    main_page = RootPage(driver)
    main_page.is_root_page()


