from pages.mainPage import MainPage
from pages.loginPage import LoginPage


def test_user_account_items(browser, correct_login):
    account_page = MainPage(browser)
    account_page.should_be_user_profile_form()
    account_page.should_be_main_account_items()


def test_logout(browser, correct_login):
    account_page = MainPage(browser)
    account_page.logout()
    login_page = LoginPage(browser)
    login_page.should_be_alert_logout()
