import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    request.cls.driver = driver
    yield driver
    driver.quit()
