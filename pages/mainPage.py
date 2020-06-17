import time

from locators.main_page import MainPageLocators
from pages.basePage import BasePage


class MainPage(BasePage):

    def should_be_success_login_alert(self):
        self.find_element(MainPageLocators.LOCATOR_ALERT_SUCCESS)

    def should_be_main_account_items(self):
        self._should_be_account_header()
        self._should_be_user_info()
        self._should_be_logout_button()

    def _should_be_account_header(self):
        account_header = self.find_element(MainPageLocators.ACCOUNT_HEADER).text
        assert account_header == "Аккаунт пользователя", "Not account page"

    def _should_be_user_info(self):
        self.find_element(MainPageLocators.USER_NAME)

    def _should_be_logout_button(self):
        self.find_element(MainPageLocators.LOGOUT_BUTTON)

    def should_be_user_profile_form(self):
        self.find_element(MainPageLocators.USER_PROFILE_FORM)

    def logout(self):
        self.find_element(MainPageLocators.LOGOUT_BUTTON).click()
        self.find_element(MainPageLocators.LOGOUT_CONFIRMATION_ACCEPT).click()
