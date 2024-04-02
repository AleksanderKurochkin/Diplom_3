import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError("Unsupported browser. Please use 'chrome' or 'firefox'.")

    css_style = "html, body { width: 100%; height: 100%; margin: 0; padding: 0; overflow: hidden; }"
    driver.execute_script(
         f"var style = document.createElement('style'); style.innerHTML = '{css_style}'; document.head.appendChild(style);")

    request.cls.driver = driver
    yield driver
    driver.quit()
