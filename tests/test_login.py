from pages.loginPage import LoginPage
from pages.mainPage import MainPage


def test_valid_login(browser, config_user_name, config_user_password):
    login_page = LoginPage(browser)
    login_page.login(config_user_name, config_user_password)
    account_page = MainPage(browser)
    account_page.should_be_success_login_alert()
    account_page.should_be_main_account_items()


def test_invalid_login(browser, config_user_name, config_incorrect_password):
    login_page = LoginPage(browser)
    login_page.login(config_user_name, config_incorrect_password)
    login_page.should_be_alert_mistake()
