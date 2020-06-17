from selenium.webdriver.common.by import By


class MainPageLocators:

    # ALERT
    LOCATOR_ALERT_SUCCESS = (By.XPATH, "//div[contains(@class, 'alert-success')]")

    # HEADER
    ACCOUNT_HEADER = (By.XPATH, "//h2//span[@translate='account.Header']")
    USER_NAME = (By.XPATH, "//a[@title='Профиль пользователя']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@ng-click='confirmLogout()']")

    # LOGOUT MODAL WINDOW
    LOGOUT_CONFIRMATION_WINDOW = (By.XPATH, "//div[text()='Выйти?']")
    LOGOUT_CONFIRMATION_ACCEPT = (By.XPATH, "//button[@ng-click='dialog.hide();']")
    LOGOUT_CONFIRMATION_CANCEL = (By.XPATH, "//button[@ng-click='dialog.cancel();']")

    # USER INFO
    USER_PROFILE_FORM = (By.XPATH, "//form[@name='AuthUserProfileForm']")
    USER_NAME_TEXTFIELD = (By.XPATH, "//input[@name='name']")
    PASSWORD_TEXTFIELD = (By.XPATH, "//input[@name='password']")
    EMAIL_TEXTFIELD = (By.XPATH, "//input[@name='email']")
    SAVE_FORM_BUTTON = (By.XPATH, "//button//span[text()='Сохранить']")

