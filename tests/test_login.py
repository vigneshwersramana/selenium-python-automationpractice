"""
This script is responsible for validating login funcnality
"""
# pylint: disable = R0801, E1101, C0103, C0116, C0301, W1201, C0115

import pytest
from loguru import logger
from pageObjects.SignInPage import SignUpandInPage
from pageObjects.HomePage import HomePage
from utilities.Base import Base
from utilities.Actions import Actions
import utilities.ReusableFunctions as reusableFunctions


class Test_Login(Base):

    @pytest.mark.positive_login
    @pytest.mark.login
    @pytest.mark.positive
    def test_validate_login(self, dataLoad):

        log = logger
        home = HomePage(self.driver)
        signIn = SignUpandInPage(self.driver)
        actions = Actions(self.driver)
        data = {}
        data = reusableFunctions.getTestCaseData(dataLoad, "TC6")

        reusableFunctions.isTitle(home.getTitle(), "My Store")
        actions.click(home.getSignInBtn())
        log.info("Clicked on Sign In Button")

        reusableFunctions.isDisplayed(signIn.getAuthenticationLbl(), "Sign In Page")

        actions.click(signIn.getEmailIdTxt())
        actions.sendKeys(signIn.getEmailIdTxt(), data.get("emailid"))
        actions.click(signIn.getPwdTxt())
        actions.sendKeys(signIn.getPwdTxt(), data.get("password"))
        actions.click(signIn.getSignInBtn())
        text = actions.getText(signIn.getMyAccountLbl())

        reusableFunctions.isText(text, "MY ACCOUNT")
        log.info("Login successful")


    @pytest.mark.negative_login
    @pytest.mark.login
    @pytest.mark.negative
    def test_validate_exception_for_missing_emailid(self, dataLoad):
        log = logger
        home = HomePage(self.driver)
        signIn = SignUpandInPage(self.driver)
        actions = Actions(self.driver)
        data = {}
        data = reusableFunctions.getTestCaseData(dataLoad, "TC6")

        title = home.getTitle()
        if title == "My Store":
            log.info("Title is " + title)
            assert True
        else:
            log.error("Title is incorrect and displayed title is " + title)
            assert False
        actions.click(home.getSignInBtn())
        log.info("Clicked on Sign In Button")

        if signIn.getAuthenticationLbl().is_displayed():
            log.info("Sign In Page loaded")
            assert True
        else:
            log.error("Sign In Page not loaded")
            assert False

        actions.click(signIn.getPwdTxt())
        actions.sendKeys(signIn.getPwdTxt(), data.get("password"))
        actions.click(signIn.getSignInBtn())
        if signIn.getEmailIdRequiredSignIn().is_displayed():
            log.info("Validation Message displayed for email id:" + actions.getText(signIn.getEmailIdRequiredSignIn()))
            assert True
        else:
            log.error("Validation Message for email id is not displayed")

    @pytest.mark.negative_login
    @pytest.mark.login
    @pytest.mark.negative
    def test_validate_exception_for_missing_password(self, dataLoad):
        log = logger
        home = HomePage(self.driver)
        signIn = SignUpandInPage(self.driver)
        actions = Actions(self.driver)
        data = {}
        data = reusableFunctions.getTestCaseData(dataLoad, "TC6")

        title = home.getTitle()
        if title == "My Store":
            log.info("Title is " + title)
            assert True
        else:
            log.error("Title is incorrect and displayed title is " + title)
            assert False
        actions.click(home.getSignInBtn())
        log.info("Clicked on Sign In Button")

        if signIn.getAuthenticationLbl().is_displayed():
            log.info("Sign In Page loaded")
            assert True
        else:
            log.error("Sign In Page not loaded")
            assert False

        actions.click(signIn.getEmailIdTxt())
        actions.sendKeys(signIn.getEmailIdTxt(), data.get("emailid"))
        actions.click(signIn.getSignInBtn())
        if signIn.getPwdRequiredSignIn().is_displayed():
            log.info("Validation Message displayed for password:" + actions.getText(signIn.getPwdRequiredSignIn()))
            assert True
        else:
            log.error("Validation Message for password is not displayed")


    @pytest.mark.negative_login
    @pytest.mark.login
    @pytest.mark.negative
    def test_validate_exception_for_invalid_email_login(self, dataLoad):

        log = logger
        home = HomePage(self.driver)
        signIn = SignUpandInPage(self.driver)
        actions = Actions(self.driver)
        data = {}
        data = reusableFunctions.getTestCaseData(dataLoad, "TC7")

        title = home.getTitle()
        if title == "My Store":
            log.info("Title is " + title)
            assert True
        else:
            log.error("Title is incorrect and displayed title is " + title)
            assert False
        actions.click(home.getSignInBtn())
        log.info("Clicked on Sign In Button")

        if signIn.getAuthenticationLbl().is_displayed():
            log.info("Sign In Page loaded")
            assert True
        else:
            log.error("Sign In Page not loaded")
            assert False

        actions.click(signIn.getEmailIdTxt())
        actions.sendKeys(signIn.getEmailIdTxt(), data.get("emailid"))
        actions.click(signIn.getPwdTxt())
        actions.sendKeys(signIn.getPwdTxt(), data.get("password"))
        actions.click(signIn.getSignInBtn())
        if signIn.getAuthenticationError().is_displayed():
            log.info("Validation Message displayed for Invalid email id:" + actions.getText(signIn.getAuthenticationErrorTxt()))
            assert True
        else:
            log.error("Validation Message for invalid email id is not displayed")

    @pytest.mark.negative_login
    @pytest.mark.login
    @pytest.mark.negative
    def test_validate_exception_for_invalid_password_login(self, dataLoad):

        log = self.getLogger()
        home = HomePage(self.driver)
        signIn = SignUpandInPage(self.driver)
        actions = Actions(self.driver)
        data = {}
        data = reusableFunctions.getTestCaseData(dataLoad, "TC8")

        title = home.getTitle()
        if title == "My Store":
            log.info("Title is " + title)
            assert True
        else:
            log.error("Title is incorrect and displayed title is " + title)
            assert False
        actions.click(home.getSignInBtn())
        log.info("Clicked on Sign In Button")

        if signIn.getAuthenticationLbl().is_displayed():
            log.info("Sign In Page loaded")
            assert True
        else:
            log.error("Sign In Page not loaded")
            assert False

        actions.click(signIn.getEmailIdTxt())
        actions.sendKeys(signIn.getEmailIdTxt(), data.get("emailid"))
        actions.click(signIn.getPwdTxt())
        actions.sendKeys(signIn.getPwdTxt(), data.get("password"))
        actions.click(signIn.getSignInBtn())
        if signIn.getAuthenticationError().is_displayed():
            log.info(
                "Validation Message displayed for Invalid password:" + actions.getText(signIn.getAuthenticationErrorTxt()))
            assert True
        else:
            log.error("Validation Message for invalid password is not displayed")
