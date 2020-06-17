import pytest
import json
from selenium import webdriver
from pages.loginPage import LoginPage

CONFIG_PATH = './configs/config.json'

capabilities = {
    "browserName": "firefox",
    "version": "76.0",
    "enableVNC": True,
    "enableVideo": False
}


@pytest.fixture
def browser(config_base_url):
    browser = webdriver.Remote(
        command_executor="http://192.168.1.100:4444/wd/hub",
        desired_capabilities=capabilities)
    browser.maximize_window()
    browser.get(config_base_url)
    yield browser
    browser.quit()


@pytest.fixture
def correct_login(browser, config_user_name, config_user_password):
    login_page = LoginPage(browser)
    login_page.login(config_user_name, config_user_password)


@pytest.fixture
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
        return data


@pytest.fixture
def config_base_url(config):
    return config['base_url']


@pytest.fixture
def config_user_name(config):
    return config['user']


@pytest.fixture
def config_user_password(config):
    return config['password']


@pytest.fixture
def config_incorrect_password(config):
    return config['incorrect_password']
