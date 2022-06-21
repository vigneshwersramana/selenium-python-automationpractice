from selenium.webdriver.support.select import Select


class Actions:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def click(element):
        element.click()

    @staticmethod
    def sendKeys(inputfield, value):
        inputfield.send_keys(value)

    @staticmethod
    def selectFromDDbyValue(dropdown, value):
        ddelement = Select(dropdown)
        ddelement.select_by_value(value)

    @staticmethod
    def selectFromDDbyText(dropdown, value):
        ddelement = Select(dropdown)
        ddelement.select_by_visible_text(value)

    @staticmethod
    def selectFromDDbyIndex(dropdown, value):
        ddelement = Select(dropdown)
        ddelement.select_by_index(value)

    @staticmethod
    def getText(element):
        return element.text

    @staticmethod
    def clear(selector):
        selector.clear()
