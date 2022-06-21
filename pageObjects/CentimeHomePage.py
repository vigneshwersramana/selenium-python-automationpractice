from selenium.webdriver.common.by import By
import utilities.ReusableFunctions as resuableFunctions


class CentimeHomePage:

    def __init__(self, driver):
        self.driver = driver

    oursolutionTxt = (By.XPATH, "//div[@aria-label='our-solutions']")
    pricingTxt = (By.XPATH, "//div[@aria-label='pricing']")
    partnersTxt = (By.XPATH, "//div[@aria-label='partners']")
    resourcesTxt = (By.XPATH, "//div[@aria-label='resources']")
    aboutUsTxt = (By.XPATH, "//div[@aria-label='about-us']")
    contactUsTxt = (By.XPATH, "//div[@aria-label='contact-us']")
    tryItFreeBtn = (By.XPATH, "//button[contains(@class,'popup-btn button')]")
    centimeKickOffTxt = (By.XPATH, "//h1[contains(text(),'Centime kick off')]")
    calendarFrm = (By.XPATH, "//iframe[contains(@src,'month=2022-05')]")
    previousMonthBtn = (By.XPATH, "//button[@aria-label='Go to previous month']")
    nextMonthBtn = (By.XPATH, "//button[@aria-label='Go to next month']")
    timeZoneTxt = (By.XPATH, "(//button[@aria-label='Timezone dropdown button']/span//following-sibling::div)[1]")
    currentMonth = (By.XPATH, "//div[@data-testid='calendar-header']/div[@data-testid='title']")
    enterDetailsTxt = (By.XPATH, "//h2[text()='Enter Details']")
    fullNameTxt = (By.XPATH, "//input[@id='full_name_input']")
    emailTxt = (By.XPATH, "//input[@id='email_input']")
    roleTxt = (By.XPATH, "//input[@name='question_0']")
    companyTxt = (By.XPATH, "//input[@name='question_1']")
    netSuiteRdBtn = (By.XPATH, "//input[@value='NetSuite']/..")
    durationTxt = (By.XPATH, "//span[contains(@class,'jrLbDfzA4kom_AzKEsEl')]/..")
    timeZoneTxt2 = (By.XPATH, "//span[contains(@class,'_Y9En91BjL0CfXc1vdwa mk_JE8xryq5hgtCt3bYN')]")
    timeDurationDateTxt = (By.XPATH, "//span[contains(@class,'NsNGp09s1QJbSbujCxAx')]/..")
    emailIDErrorMsg = (By.XPATH, "//div[@data-component='error-message']")
    scheduleEventButton = (By.XPATH, "//button[@type='submit']")

    def getEmailIDErrorMsg(self):
        return resuableFunctions.waitForElementVisible(self.driver, CentimeHomePage.emailIDErrorMsg, interval=20)

    def getScheduleEventButton(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.scheduleEventButton, interval=20)

    def getEnterDetailsTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.enterDetailsTxt, interval=20)

    def getDurationTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.durationTxt, interval=20)

    def getTimeZoneTxt2(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.timeZoneTxt2, interval=20)

    def getTimeDurationDateTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.timeDurationDateTxt, interval=20)

    def getNetSuiteRdBtn(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.netSuiteRdBtn, interval=20)

    def getFullNameTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.fullNameTxt, interval=20)

    def getEmailTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.emailTxt, interval=20)

    def getRoleTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.roleTxt, interval=20)

    def getCompanyTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.companyTxt, interval=20)

    def getOursolutionTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.oursolutionTxt, interval=20)

    def getPricingTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.pricingTxt, interval=20)

    def getPartnersTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.partnersTxt, interval=20)

    def getResourcesTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.resourcesTxt, interval=20)

    def getAboutUsTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.aboutUsTxt, interval=20)

    def getContactUsTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.contactUsTxt, interval=20)

    def getPreviousMonthBtn(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.previousMonthBtn, interval=20)

    def getNextMonthBtn(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.nextMonthBtn, interval=20)

    def getTryItFreeBtn(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.tryItFreeBtn, interval=20)

    def getCalendarFrm(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.calendarFrm, interval=20)

    def getCentimeKickOffTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.centimeKickOffTxt, interval=20)

    def getTimeZoneTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.timeZoneTxt, interval=20)

    def getCurrentMonth(self):
        return resuableFunctions.waitForElementPresence(self.driver, CentimeHomePage.currentMonth, interval=20)

    def getCreateDate(self, date):
        dateBtn = (By.XPATH,"//button/span[contains(text(),'"+ date + "')]")
        return resuableFunctions.waitForElementPresence(self.driver, dateBtn, interval=20)

    def getCreateConfirmBtn(self, time):
        confirmBtn = (By.XPATH, "//button[@aria-label='Confirm "+ time + "']")
        return resuableFunctions.waitForElementVisible(self.driver, confirmBtn, interval=20)

    def getCreateTimeBtn(self, time):
        timeBtn = (By.XPATH, "//button[@data-start-time='"+ time + "']")
        return resuableFunctions.waitForElementVisible(self.driver, timeBtn, interval=20)

    def getTitle(self):
        return resuableFunctions.getTitle(self.driver)






