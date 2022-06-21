from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger


def waitTobeClickable(driver, selector, interval):
    try:
        return WebDriverWait(driver, interval).until(EC.element_to_be_clickable(selector))
    except TimeoutException:
        logger.error("Time out waiting for element to be clickable")


def waitForElementPresence(driver, selector, interval):
    try:
        return WebDriverWait(driver, interval).until(EC.presence_of_element_located(selector))
    except TimeoutException:
        logger.error("Time out waiting for element to be present on the page")

def waitForElementVisible(driver, selector, interval):
    try:
        return WebDriverWait(driver, interval).until(EC.visibility_of_element_located(selector))
    except TimeoutException:
        logger.error("Time out waiting for element to be present on the page")


def waitForElementNotPresent(driver, selector, interval):
    try:
        return WebDriverWait(driver, interval).until(EC.invisibility_of_element_located(selector))
    except TimeoutException:
        logger.error("Time out waiting for element to be present on the page")


def waitForTitle(driver, title, interval):
    try:
        return WebDriverWait(driver, interval).until(EC.title_is(title))
    except TimeoutException:
        logger.error("Time out waiting for Page title")


def isPresent(driver, selector):
    try:
        driver.findElement(selector)
    except NoSuchElementException:
        # if element not exist
        return False
    return True


def isDisplayed(selector, text):
    if selector.is_displayed():
        logger.info(text + ": Element is Displayed")
        assert True
    else:
        logger.error(text + ": Element is not Displayed")
        assert False


def getTitle(driver):
    return driver.title


def getTestCaseData(data, testCaseKey):
    for eachTestCaseKey in data["testcases"]:
        if testCaseKey == eachTestCaseKey["testcaseid"]:
            data_dict = eachTestCaseKey
            break
    return data_dict


def isTitle(title, expectedTitle):
    if title == expectedTitle:
        logger.info("Title is " + title)
        assert True
    else:
        logger.error("Title is incorrect and displayed title is " + title)
        assert False


def isText(text, expectedText):
    if text == expectedText:
        logger.info("Text Matches and text is " + text)
        assert True
    else:
        logger.error("Text are not Equal" + text)
        assert False


def containsText(text, expectedText):
    if expectedText in text:
        logger.info("Text Matches and text is " + expectedText)
        assert True
    else:
        logger.error("Text are not Equal" + expectedText)
        assert False

def switchToFrame(driver, selector):
    driver.switch_to.frame(selector)
