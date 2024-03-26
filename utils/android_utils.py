import re
import logging
from appium.options.android import UiAutomator2Options
from utils.utils import run_cmd_with_output


capabilities = {
    'autoGrantPermissions': True,
    'automationName': 'uiautomator2',
    'newCommandTimeout': 500,
    'noSign': True,
    'platformName': 'Android',
    'platformVersion': '12.0',
    'resetKeyboard': True,
    'systemPort': 8301,
    'takesScreenshot': True,
    'deviceName': 'Android',
    'udid': None,
    'appPackage': 'com.ajaxsystems',
    'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}


def get_device_uid():
    cmd = "adb devices"
    out, err = run_cmd_with_output(cmd, shell=True)
    if err or not out:
        raise Exception(f"Not found active device\n{err}")
    uid = re.findall(r'(emulator-\d+)', out)[0]
    logging.info(f"Device {uid=}")
    return uid


def get_android_desired_capabilities():
    capabilities['udid'] = get_device_uid()
    return UiAutomator2Options().load_capabilities(capabilities)
