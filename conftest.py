import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# must be like ".../" without culture
BASIC_URL = "sorry it's a secret"


def log_setup():
    logger = logging.getLogger()
    file_handler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)


log_setup()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def driver_fixture(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'firefox':
        service_obj = Service("drivers/geckodriver.exe")
        driver = webdriver.Firefox(firefox_binary=r"C:\Program Files\Mozilla Firefox\Firefox.exe", service=service_obj)

    else:
        service_obj = Service("drivers/chromedriver.exe")
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # to not close the browser after execution
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)

    driver.implicitly_wait(1)
    driver.maximize_window()
    driver.get(BASIC_URL)
    request.cls.driver = driver

    # closes browser and session after test. Comment 2 lines below when do not need to close the browser after test
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def pages():
    dictionary_with_pages = {}
    return dictionary_with_pages


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            item.cls.driver.get_screenshot_as_file(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
