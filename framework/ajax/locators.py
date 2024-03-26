from appium.webdriver.common.appiumby import AppiumBy


class RootPageLocators:
    LOGIN_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log in"]')
    CREATE_ACCOUNT_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Create account"]')


class LoginPageLocators:
    EMAIL_FIELD = (AppiumBy.ID, 'com.ajaxsystems:id/authLoginEmail')
    PASSWORD_FIELD = (AppiumBy.ID, 'com.ajaxsystems:id/authLoginPassword')
    FORGOT_PASSWORD_LINK = (AppiumBy.ID, 'com.ajaxsystems:id/authLoginForgotPassword')
    AUTOLOGIN_BUTTON = (AppiumBy.ID, 'com.ajaxsystems:id/authLogin')
    INVALID_MESSAGE = (AppiumBy.ID, 'com.ajaxsystems:id/snackbar_text')


class MainPageLocators:
    MENU_DRAWER = (AppiumBy.ID, 'com.ajaxsystems:id/menuDrawer')
    APP_SETTINGS = (AppiumBy.ID, 'com.ajaxsystems:id/settings')
    HELP = (AppiumBy.ID, 'com.ajaxsystems:id/help')
    REPORT_PROBLEM = (AppiumBy.ID, 'com.ajaxsystems:id/logs')
    ADD_SPACE = (AppiumBy.ID, 'com.ajaxsystems:id/addSpace')
    TERM_OF_SERVICE = (AppiumBy.ID, 'com.ajaxsystems:id/documentation_text')


class SettingsPageLocators:
    LOG_OUT = (AppiumBy.ID, 'com.ajaxsystems:id/accountInfoLogoutNavigate')
