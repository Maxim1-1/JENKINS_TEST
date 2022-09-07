import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser_fixture(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
       driver = webdriver.Chrome(ChromeDriverManager().install())
    if browser == 'firefox':
       driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    yield driver
    driver.quit()
