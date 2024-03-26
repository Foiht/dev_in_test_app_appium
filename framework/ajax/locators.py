from appium.webdriver.common.appiumby import AppiumBy


class RootPageLocators:
    LOGIN_BUTTON = (AppiumBy.XPATH, '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[1]/android.view.View/android.view.View/android.widget.Button')
    CREATE_ACCOUNT_BUTTON = (AppiumBy.XPATH, '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[2]/android.view.View/android.view.View/android.widget.Button')


class LoginPageLocators:
    EMAIL_FIELD = (AppiumBy.ID, 'com.ajaxsystems:id/authLoginEmail')
    PASSWORD_FIELD = (AppiumBy.ID, 'com.ajaxsystems:id/authLoginPassword')
    FORGOT_PASSWORD_LINK = (AppiumBy.ID, 'com.ajaxsystems:id/authLoginForgotPassword')
    AUTOLOGIN_BUTTON = (AppiumBy.ID, 'com.ajaxsystems:id/authLogin')
    INVALID_MESSAGE = (AppiumBy.ID, 'com.ajaxsystems:id/snackbar_text')


class MainPageLocators:
    MENU_DRAWER = (AppiumBy.ID, 'com.ajaxsystems:id/menuDrawer')
    APP_SETTINGS = (AppiumBy.ID, 'com.ajaxsystems:id/setting')
    HELP = (AppiumBy.ID, 'com.ajaxsystems:id/help')
    REPORT_PROBLEM = (AppiumBy.ID, 'com.ajaxsystems:id/logs')
    ADD_SPACE = (AppiumBy.ID, 'com.ajaxsystems:id/addSpace')


class SettingsPageLocators:
    LOG_OUT = (AppiumBy.ID, 'com.ajaxsystems:id/accountInfoLogoutNavigate')
