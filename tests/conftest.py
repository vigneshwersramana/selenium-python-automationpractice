"""
This script is responsible setting up the requried configuration for execution
"""
# pylint: disable = R0801, E1101, C0103, C0116, C0301, W0603, R1714, C0411,W1514, C0209, R1732

import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pathlib import Path
from utilities.Base import Base
from loguru import logger

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://automationpractice.com/index.php")
    parser.addoption("--app", action="store", default="automationpractice")


@pytest.fixture(scope="function")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    url = request.config.getoption("url")
    app = request.config.getoption("app")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))


    if app == "centime":
        driver.get("https://www.centime.com/")
    else:
        driver.get(url)

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


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
            tc_name = report.nodeid.split("::")[-1]
            # tc_name = re.sub(r'\[.*\]', '', tc_name)
            file_name = Base.ROOT_PATH + "/reports/screenshots/" + tc_name + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="screenshots/%s.png" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % tc_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.save_screenshot(name)


@pytest.fixture(autouse=True)
def write_logs(request):
    # put logs in tests/logs
    ROOT_PATH = str(Path(__file__).parent.parent)
    log_path = Path(ROOT_PATH + "/logs")

    # tidy logs in subdirectories based on test module and class names
    module = request.module
    class_ = request.cls
    name = request.node.name + ".log"

    if module:
        log_path /= module.__name__.replace("tests.", "")
    if class_:
        log_path /= class_.__name__

    log_path.mkdir(parents=True, exist_ok=True)

    # append last part of the name
    log_path /= name

    # enable the logger
    logger.remove()
    logger.configure(handlers=[{"sink": log_path, "level": "TRACE", "mode": "w"}])
    # logger.basicConfig(filename=name, level=logging.INFO)
    logger.info(":::::::::::::::::::::::::::::::::::::::::")
    logger.info("Test Execution Started: " + request.node.name)
    logger.enable("my_package")


@pytest.fixture()
def dataLoad():
    testDataFile = {}
    testDataFile = json.loads((open(Base.ROOT_PATH + "/resources/input_data.json", 'r').read()))
    return testDataFile
