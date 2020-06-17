from selenium.common.exceptions import NoSuchElementException

from pages.basePage import BasePage
from locators.login_page import LoginPageLocators


class LoginPage(BasePage):

    def login(self, login, password):
        self._enter_username(username=login)
        self._enter_password(password=password)
        self._click_login_button()

    def _enter_username(self, username):
        username_text_field = self.find_element(LoginPageLocators.USERNAME_TEXTFIELD)
        username_text_field.click()
        username_text_field.send_keys(username)

    def _enter_password(self, password):
        password_text_field = self.find_element(LoginPageLocators.PASSWORD_TEXTFIELD)
        password_text_field.click()
        password_text_field.send_keys(password)

    def _click_login_button(self):
        login_button = self.find_element(LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def should_be_alert_mistake(self):
        self.find_element(LoginPageLocators.ALERT_MISTAKE)

    def should_be_alert_logout(self):
        self.find_element(LoginPageLocators.ALERT_LOGOUT)
