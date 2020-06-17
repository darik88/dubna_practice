from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//form[@name='loginFormForm']")
    USERNAME_TEXTFIELD = (By.XPATH, "//input[@name='login']")
    PASSWORD_TEXTFIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='btn btn-default']")
    ALERT_MISTAKE = (By.XPATH, "//div[contains(@class, 'alert-danger')]")
    ALERT_LOGOUT = (By.XPATH, "//div[contains(@class, 'alert-info')]")