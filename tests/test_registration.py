"""
This script is responsible for validating registration funcnality
"""
# pylint: disable = R0801, E1101, C0103, C0116, C0301, C0115

import random
import string
import pytest
from loguru import logger
import utilities.ReusableFunctions as reusableFunctions
from pageObjects.HomePage import HomePage
from pageObjects.SignInPage import SignUpandInPage
from utilities.Actions import Actions
from utilities.Base import Base


class Test_Registration(Base):

    @pytest.mark.registration
    @pytest.mark.positive_registration
    @pytest.mark.positive
    def test_registration(self, dataLoad):
        log = logger
        home = HomePage(self.driver)
        signIn = SignUpandInPage(self.driver)
        actions = Actions(self.driver)
        data = reusableFunctions.getTestCaseData(dataLoad, "TC1")

        home.getTitle()
        reusableFunctions.isTitle(home.getTitle(), "My Store")
        actions.click(home.getSignInBtn())
        log.info("Clicked on Sign In Button")

        reusableFunctions.isDisplayed(signIn.getAuthenticationLbl(), "Sign In Page")

        actions.click(signIn.getEmailIDCreate())
        n = 3
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=n))
        emailIdGenerated = str(res) + data.get("emailid")
        actions.sendKeys(signIn.getEmailIDCreate(), emailIdGenerated)
        actions.click(signIn.getCreateAccountBtn())

        reusableFunctions.isDisplayed(signIn.getPersonalInformationLbl(), "Registration Form")
        actions.click(signIn.getMrRdBtn())
        reusableFunctions.isDisplayed(signIn.getPersonalInformationLbl(), "Personal Information")
        actions.sendKeys(signIn.getCustFirstNameTxt(), data.get("firstname"))
        actions.sendKeys(signIn.getCustLastNameTxt(), data.get("lastname"))
        emaiId = signIn.getEmailIdTxt().get_attribute('value')
        assert emailIdGenerated == emaiId
        actions.sendKeys(signIn.getPasswordTxt(), data.get("password"))
        date = data.get("dob").split("-")
        actions.selectFromDDbyValue(signIn.getDaysOpt(), date[0])
        actions.selectFromDDbyValue(signIn.getMonthOpt(), date[1])
        actions.selectFromDDbyValue(signIn.getYearsOpt(), date[2])
        actions.click(signIn.getNewsLetterChk())
        actions.click(signIn.getOfferChk())
        # assert actions.getText(signIn.getFirstNameTxt()) == data.get("firstname")
        # assert actions.getText(signIn.getLastNameTxt()) == data.get("lastname")
        actions.sendKeys(signIn.getCompanyTxt(), data.get("company"))
        actions.sendKeys(signIn.getAddress1Txt(), data.get("address1"))
        actions.sendKeys(signIn.getAddress2Txt(), data.get("address2"))
        actions.sendKeys(signIn.getCityTxt(), data.get("city"))
        actions.sendKeys(signIn.getAddress1Txt(), data.get("address1"))
        actions.selectFromDDbyText(signIn.getStateOpt(), data.get("state"))
        actions.sendKeys(signIn.getPostCodeTxt(), data.get("postalcode"))
        assert actions.getText(signIn.getCountryNameTxt()) == "United States"
        actions.sendKeys(signIn.getAdditionalInfoTextArea(), data.get("additionalinfo"))
        actions.sendKeys(signIn.getHomePhoneTxt(), data.get("homenumber"))
        actions.sendKeys(signIn.getMobilePhoneTxt(), data.get("mobilenumber"))
        # actions.click(signIn.getSubmitBtn())
        # reusableFunctions.isDisplayed(signIn.getSuccessMsg(), "Account logged In")

    @pytest.mark.negative_registration
    @pytest.mark.registration
    @pytest.mark.negative
    def test_validate_exception_registration_for_existing_emailid(self, dataLoad):
        log = logger
        home = HomePage(self.driver)
        signIn = SignUpandInPage(self.driver)
        actions = Actions(self.driver)
        data = reusableFunctions.getTestCaseData(dataLoad, "TC2")

        home.getTitle()
        reusableFunctions.isTitle(home.getTitle(), "My Store")
        actions.click(home.getSignInBtn())
        log.info("Clicked on Sign In Button")

        reusableFunctions.isDisplayed(signIn.getAuthenticationLbl(), "Sign In Page")

        actions.click(signIn.getEmailIDCreate())
        actions.sendKeys(signIn.getEmailIDCreate(), data.get("emailid"))
        actions.click(signIn.getCreateAccountBtn())

        reusableFunctions.isDisplayed(signIn.getCreateAccountErrorMsg(), "Email ID Already Registered")


    @pytest.mark.negative_registration
    @pytest.mark.registration
    @pytest.mark.negative
    def test_validate_exception_registration_for_invalid_emailid(self, dataLoad):
        log = logger
        home = HomePage(self.driver)
        signIn = SignUpandInPage(self.driver)
        actions = Actions(self.driver)
        data = reusableFunctions.getTestCaseData(dataLoad, "TC3")

        home.getTitle()
        reusableFunctions.isTitle(home.getTitle(), "My Store")
        actions.click(home.getSignInBtn())
        log.info("Clicked on Sign In Button")

        reusableFunctions.isDisplayed(signIn.getAuthenticationLbl(), "Sign In Page")

        actions.click(signIn.getEmailIDCreate())
        actions.sendKeys(signIn.getEmailIDCreate(), data.get("emailid"))
        actions.click(signIn.getCreateAccountBtn())

        reusableFunctions.isDisplayed(signIn.getCreateEmailIdInvalidError(), "Invalid Email Id entered ")

    @pytest.mark.registration
    @pytest.mark.negative_registration
    @pytest.mark.negative
    def test_validate_exception_for_mandatory_fields_in_registration(self, dataLoad):
        log = logger
        home = HomePage(self.driver)
        signIn = SignUpandInPage(self.driver)
        actions = Actions(self.driver)
        data = reusableFunctions.getTestCaseData(dataLoad, "TC4")

        home.getTitle()
        reusableFunctions.isTitle(home.getTitle(), "My Store")
        actions.click(home.getSignInBtn())
        log.info("Clicked on Sign In Button")

        reusableFunctions.isDisplayed(signIn.getAuthenticationLbl(), "Sign In Page")

        actions.click(signIn.getEmailIDCreate())
        actions.sendKeys(signIn.getEmailIDCreate(), data.get("emailid"))
        actions.click(signIn.getCreateAccountBtn())

        reusableFunctions.isDisplayed(signIn.getPersonalInformationLbl(), "Registration Form")
        signIn.getAliasAddrTxt().clear()
        actions.click(signIn.getSubmitBtn())
        reusableFunctions.isDisplayed(signIn.getErrorDetails(), "Error Details List")
        reusableFunctions.isDisplayed(signIn.getAtleastOnePhNumberError(),
                                      "You must register at least one phone number")
        reusableFunctions.isDisplayed(signIn.getLastNameRequiredError(), "Last Name is required")
        reusableFunctions.isDisplayed(signIn.getFirstNameRequiredError(), "First Name is required")
        reusableFunctions.isDisplayed(signIn.getPasswordRequiredError(), "Password is required")
        reusableFunctions.isDisplayed(signIn.getAddress1Txt(), "Address 1 is required")
        reusableFunctions.isDisplayed(signIn.getCityRequiredError(), "City is required")
        reusableFunctions.isDisplayed(signIn.getStateRequiredError(), "State is Required")
        reusableFunctions.isDisplayed(signIn.getPostalCodeRequiredError(), "Postal Code is Required")
        reusableFunctions.isDisplayed(signIn.getAliasRequiredError(), "Alias is Required")

    @pytest.mark.registration
    @pytest.mark.negative_registration
    @pytest.mark.negative
    def test_validate_exception_for_country_registration(self, dataLoad):
        log = logger
        home = HomePage(self.driver)
        signIn = SignUpandInPage(self.driver)
        actions = Actions(self.driver)
        data = reusableFunctions.getTestCaseData(dataLoad, "TC4")

        home.getTitle()
        reusableFunctions.isTitle(home.getTitle(), "My Store")
        actions.click(home.getSignInBtn())
        log.info("Clicked on Sign In Button")

        reusableFunctions.isDisplayed(signIn.getAuthenticationLbl(), "Sign In Page")

        actions.click(signIn.getEmailIDCreate())
        actions.sendKeys(signIn.getEmailIDCreate(), data.get("emailid"))
        actions.click(signIn.getCreateAccountBtn())

        reusableFunctions.isDisplayed(signIn.getPersonalInformationLbl(), "Registration Form")
        actions.selectFromDDbyText(signIn.getCountryOpt(), "-")
        actions.click(signIn.getSubmitBtn())
        reusableFunctions.isDisplayed(signIn.getErrorDetails(), "Error Details List")
        reusableFunctions.isDisplayed(signIn.getCountryRequiredError(), "Country is required")
        reusableFunctions.isDisplayed(signIn.getCountryInvalidError(), "Country is Invalid")
        reusableFunctions.isDisplayed(signIn.getCountryLoadError(), "Country not loaded")

    @pytest.mark.registration
    @pytest.mark.negative_registration
    @pytest.mark.negative
    def test_validate_exception_for_invalid_registration(self, dataLoad):
        log = logger
        home = HomePage(self.driver)
        signIn = SignUpandInPage(self.driver)
        actions = Actions(self.driver)
        data = reusableFunctions.getTestCaseData(dataLoad, "TC5")

        home.getTitle()
        reusableFunctions.isTitle(home.getTitle(), "My Store")
        actions.click(home.getSignInBtn())
        log.info("Clicked on Sign In Button")

        reusableFunctions.isDisplayed(signIn.getAuthenticationLbl(), "Sign In Page")

        actions.click(signIn.getEmailIDCreate())
        actions.sendKeys(signIn.getEmailIDCreate(), data.get("emailid"))
        actions.click(signIn.getCreateAccountBtn())

        reusableFunctions.isDisplayed(signIn.getPersonalInformationLbl(), "Registration Form")
        actions.sendKeys(signIn.getCustFirstNameTxt(), data.get("firstname"))
        actions.sendKeys(signIn.getCustLastNameTxt(), data.get("lastname"))
        actions.clear(signIn.getEmailIdTxt())
        actions.sendKeys(signIn.getEmailIdTxt(), data.get("emailinvalid"))
        actions.sendKeys(signIn.getPasswordTxt(), data.get("password"))
        #add code to move page
        actions.click(signIn.getPostCodeTxt())
        actions.sendKeys(signIn.getPostCodeTxt(), data.get("postalcode"))
        actions.sendKeys(signIn.getHomePhoneTxt(), data.get("homenumber"))
        actions.sendKeys(signIn.getMobilePhoneTxt(), data.get("mobilenumber"))
        actions.click(signIn.getSubmitBtn())
        reusableFunctions.isDisplayed(signIn.getErrorDetails(), "Error Details List")
        reusableFunctions.isDisplayed(signIn.getFirstNameInvalidError(), "First Name is Invalid")
        reusableFunctions.isDisplayed(signIn.getLastNameInvalidError(), "Last Name is Invalid")
        reusableFunctions.isDisplayed(signIn.getEmailIdInvalidError(), "Email Id is Invalid")
        reusableFunctions.isDisplayed(signIn.getPasswordInvalidError(), "Password is Invalid")
        reusableFunctions.isDisplayed(signIn.getPostalCodeRequiredError(), "Postal Code is Invalid")
        reusableFunctions.isDisplayed(signIn.getHomePhoneNumberError(), "Home Number is Invalid")
        reusableFunctions.isDisplayed(signIn.getMobilePhoneNumberError(), "Mobile Number is Invalid")
