"""
This script is responsible for validating centime customer connect
"""
# pylint: disable = R0801, E1101, C0103, C0116, C0301, C0115

import pytest
import utilities.ReusableFunctions as reusableFunctions
from pageObjects.CentimeHomePage import CentimeHomePage
from utilities.Actions import Actions
from utilities.Base import Base


class Test_Centime(Base):

    @pytest.mark.centime
    @pytest.mark.positive
    def test_event_scheduler_centime(self, dataLoad):
        centime = CentimeHomePage(self.driver)
        actions = Actions(self.driver)
        data = {}
        data = reusableFunctions.getTestCaseData(dataLoad, "TC11")

        self.driver.get("https://www.centime.com/")
        reusableFunctions.isTitle(centime.getTitle(), "Centime Cash Flow Management")

        reusableFunctions.isDisplayed(centime.getOursolutionTxt(), "Our Solutions")
        reusableFunctions.isDisplayed(centime.getPricingTxt(), "Pricing")
        reusableFunctions.isDisplayed(centime.getPartnersTxt(), "Partners")
        reusableFunctions.isDisplayed(centime.getResourcesTxt(), "Resources")
        reusableFunctions.isDisplayed(centime.getAboutUsTxt(), "About Us")
        reusableFunctions.isDisplayed(centime.getContactUsTxt(), "Contact Us")

        actions.click(centime.getTryItFreeBtn())
        reusableFunctions.switchToFrame(self.driver, centime.getCalendarFrm())
        reusableFunctions.isDisplayed(centime.getCentimeKickOffTxt(), "Centime Kick Off")
        reusableFunctions.isDisplayed(centime.getTimeZoneTxt(), "IST Time Zone")
        actions.click(centime.getCreateDate(data.get("date")))
        actions.click(centime.getCreateTimeBtn(data.get("time")))
        actions.click(centime.getCreateConfirmBtn(data.get("time")))

        reusableFunctions.isDisplayed(centime.getEnterDetailsTxt(), "Enter Details")
        reusableFunctions.containsText(actions.getText(centime.getDurationTxt()), "30 min")
        reusableFunctions.containsText(actions.getText(centime.getTimeZoneTxt2()), "India Standard Time")
        reusableFunctions.isDisplayed(centime.getTimeDurationDateTxt(), actions.getText(centime.getTimeDurationDateTxt()))
        actions.sendKeys(centime.getFullNameTxt(), data.get("name"))
        actions.sendKeys(centime.getEmailTxt(), data.get("emailid"))
        actions.sendKeys(centime.getRoleTxt(), data.get("role"))
        actions.sendKeys(centime.getCompanyTxt(), data.get("company"))
        actions.click(centime.getNetSuiteRdBtn())

    @pytest.mark.centime
    @pytest.mark.negative
    def test_validate_exception_for_emailid_centime(self, dataLoad):
        centime = CentimeHomePage(self.driver)
        actions = Actions(self.driver)
        data = {}
        data = reusableFunctions.getTestCaseData(dataLoad, "TC12")

        self.driver.get("https://www.centime.com/")
        reusableFunctions.isTitle(centime.getTitle(), "Centime Cash Flow Management")

        reusableFunctions.isDisplayed(centime.getOursolutionTxt(), "Our Solutions")
        reusableFunctions.isDisplayed(centime.getPricingTxt(), "Pricing")
        reusableFunctions.isDisplayed(centime.getPartnersTxt(), "Partners")
        reusableFunctions.isDisplayed(centime.getResourcesTxt(), "Resources")
        reusableFunctions.isDisplayed(centime.getAboutUsTxt(), "About Us")
        reusableFunctions.isDisplayed(centime.getContactUsTxt(), "Contact Us")

        actions.click(centime.getTryItFreeBtn())
        reusableFunctions.switchToFrame(self.driver, centime.getCalendarFrm())
        reusableFunctions.isDisplayed(centime.getCentimeKickOffTxt(), "Centime Kick Off")
        reusableFunctions.isDisplayed(centime.getTimeZoneTxt(), "IST Time Zone")
        actions.click(centime.getCreateDate(data.get("date")))
        actions.click(centime.getCreateTimeBtn(data.get("time")))
        actions.click(centime.getCreateConfirmBtn(data.get("time")))

        reusableFunctions.isDisplayed(centime.getEnterDetailsTxt(), "Enter Details")
        reusableFunctions.containsText(actions.getText(centime.getDurationTxt()), "30 min")
        reusableFunctions.containsText(actions.getText(centime.getTimeZoneTxt2()), "India Standard Time")
        reusableFunctions.isDisplayed(centime.getTimeDurationDateTxt(),
                                      actions.getText(centime.getTimeDurationDateTxt()))
        actions.sendKeys(centime.getFullNameTxt(), data.get("name"))
        actions.sendKeys(centime.getEmailTxt(), data.get("emailid"))
        actions.sendKeys(centime.getRoleTxt(), data.get("role"))
        actions.sendKeys(centime.getCompanyTxt(), data.get("company"))
        actions.click(centime.getNetSuiteRdBtn())
        actions.click(centime.getScheduleEventButton())
        reusableFunctions.isDisplayed(centime.getEmailIDErrorMsg(), "Invalid Email Entered")
