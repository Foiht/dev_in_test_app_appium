from appium.webdriver.common.appiumby import AppiumBy


class RootPageLocators:
    LOGIN_BUTTON = (AppiumBy.XPATH, '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[1]/android.view.View/android.view.View/android.widget.Button')
    CREATE_ACCOUNT_BUTTON = (AppiumBy.XPATH, '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[2]/android.view.View/android.view.View/android.widget.Button')


class LoginPageLocators:
    EMAIL_FIELD = (AppiumBy.ID, 'com.ajaxsystems:id/authLoginEmail')
    PASSWORD_FIELD = (AppiumBy.ID, 'com.ajaxsystems:id/authLoginPassword')
    FORGOT_PASSWORD_LINK = (AppiumBy.ID, 'com.ajaxsystems:id/authLoginForgotPassword')
    AUTOLOGIN_BUTTON = (AppiumBy.ID, 'com.ajaxsystems:id/authLogin')

