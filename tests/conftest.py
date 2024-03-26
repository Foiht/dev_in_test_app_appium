import logging
import subprocess
import time
from pathlib import Path

import pytest
from appium import webdriver

from modules import logger
from utils.android_utils import get_android_desired_capabilities
from utils.utils import release_port


@pytest.fixture(autouse=True)
def run_test_setup_teardown(request):
    """Fixture to set up and teardown test execution"""
    logging.info("=============== START TEST '{}' =============== ".format(request.node.name))
    yield
    logging.info("=============== FINISH TEST '{}' =============== ".format(request.node.name))


def pytest_configure(config):
    config.base_path = Path(__file__).parent.parent
    logger.initialize(config.base_path)


@pytest.fixture(scope='session')
def run_appium_server():
    port = 4723
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', str(port), '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    logging.info("Starting appium server")
    time.sleep(5)
    yield
    logging.info("Stopping appium server")
    subprocess.call(['pkill', 'appium'])
    release_port(port)


@pytest.fixture
def driver(run_appium_server):
    driver = webdriver.Remote('http://localhost:4723', options=get_android_desired_capabilities())
    logging.info("Webdriver started")
    yield driver
    if driver:
        logging.info("Webdriver stopped")
        driver.quit()


@pytest.fixture(scope='module')
def driver_module(run_appium_server):
    driver = webdriver.Remote('http://localhost:4723', options=get_android_desired_capabilities())
    logging.info("Webdriver started")
    yield driver
    if driver:
        logging.info("Webdriver stopped")
        driver.quit()
