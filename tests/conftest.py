import pytest
import json
from selenium import webdriver
from pages.loginPage import LoginPage

CONFIG_PATH = './configs/config.json'
SUPPORTED_BROWSERS = ['chrome', 'firefox']


@pytest.fixture
def browser(config_os, config_browser, config_base_url):
    if config_os == "win":
        if config_browser == "firefox":
            browser = webdriver.Firefox(executable_path="./drivers/geckodriver.exe")
        elif config_browser == "chrome":
            browser = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        else:
            raise Exception(f'"{config_browser}" is not a supported browser')
    elif config_os == "linux":
        if config_browser == "firefox":
            browser = webdriver.Firefox(executable_path="drivers/geckodriver")
        elif config_browser == "chrome":
            browser = webdriver.Chrome(executable_path="drivers/chromedriver")
        else:
            raise Exception(f'"{config_browser}" is not a supported browser')
    else:
        raise Exception(f"{config_os} is not supported OS")

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
def config_os(config):
    return config['os']


@pytest.fixture
def config_browser(config):
    if "browser" not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


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
