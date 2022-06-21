from selenium.webdriver.common.by import By
import utilities.ReusableFunctions as resuableFunctions


class SignUpandInPage:

    def __init__(self, driver):
        self.driver = driver

    # Create Account Locators
    authenticationLbl = (By.XPATH, "//h1[text()='Authentication']")
    createAnAccountLbl = (By.XPATH, "//h3[text()='Create an account']")
    emailIDCreate = (By.ID, "email_create")
    createAccountBtn = (By.NAME, "SubmitCreate")

    def getAuthenticationLbl(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.authenticationLbl, interval=20)

    def getCreateAnAccountLbl(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.createAnAccountLbl, interval=20)

    def getEmailIDCreate(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.emailIDCreate, interval=20)

    def getCreateAccountBtn(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.createAccountBtn, interval=20)

    # Create Account Error Details Locators
    createAccountErrorMsg = (By.XPATH, "//div[@id='create_account_error']//li")
    createEmailIdInvalidError = (By.XPATH, "//li[contains(text(),'Invalid email address.')]")

    def getCreateAccountErrorMsg(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.createAccountErrorMsg, interval=20)

    def getCreateEmailIdInvalidError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.createEmailIdInvalidError, interval=20)

    # SignIn Locators
    emailIdTxt = (By.ID, "email")
    pwdTxt = (By.ID, "passwd")
    signInBtn = (By.ID, "SubmitLogin")
    forgotPwdLnk = (By.XPATH, "//a[text()='Forgot your password?']")
    myAccountLbl = (By.XPATH, "//h1[text()='My account']")
    homePageLogo = (By.XPATH, "//div[@id='header_logo']")

    def getHomePageLogo(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.homePageLogo, interval=20)

    def getAlreadyRegisteredLbl(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.alreadyRegisteredLbl, interval=20)

    def getEmailIdTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.emailIdTxt, interval=20)

    def getPwdTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.pwdTxt, interval=20)

    def getSignInBtn(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.signInBtn, interval=20)

    def getForgotPwdLnk(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.forgotPwdLnk, interval=20)

    def getMyAccountLbl(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.myAccountLbl, interval=20)

    # Sign In Error
    emailIdRequiredSignIn = (By.XPATH, "//li[contains(text(),'An email address required.')]")
    pwdRequiredSignIn = (By.XPATH, "//li[contains(text(),'Password is required.')]")
    authenticationError = (By.XPATH, "//li[contains(text(),'Authentication failed.')]")
    authenticationErrorTxt = (By.XPATH, "//div[@class='alert alert-danger']/ol/li")

    def getEmailIdRequiredSignIn(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.emailIdRequiredSignIn, interval=20)

    def getPwdRequiredSignIn(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.pwdRequiredSignIn, interval=20)

    def getAuthenticationError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.authenticationError, interval=20)

    def getAuthenticationErrorTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.authenticationErrorTxt, interval=20)

    # Registration Page Locators
    personalInformationLbl = (By.XPATH, "//h3[contains(text(),'Your personal information')]")
    mrRdBtn = (By.ID, "id_gender1")
    mrsRdBtn = (By.ID, "id_gender1")
    custFirstNameTxt = (By.ID, "customer_firstname")
    custLastNameTxt = (By.ID, "customer_lastname")
    emailIDTxt = (By.ID, "email")
    passwordTxt = (By.ID, "passwd")
    daysOpt = (By.ID, "days")
    monthsOpt = (By.ID, "months")
    yearsOpt = (By.ID, "years")
    firstNameTxt = (By.ID, "firstname")
    lastNameTxt = (By.ID, "lastname")
    companyTxt = (By.ID, "company")
    address1Txt = (By.ID, "address1")
    address2Txt = (By.ID, "address2")
    cityTxt = (By.ID, "city")
    stateOpt = (By.ID, "id_state")
    postCodeTxt = (By.ID, "postcode")
    countryOpt = (By.ID, "id_country")
    additionalInfoTextArea = (By.ID, "other")
    homePhoneTxt = (By.ID, "phone")
    mobilePhoneTxt = (By.ID, "phone_mobile")
    aliasAddrTxt = (By.ID, "alias")
    submitBtn = (By.ID, "submitAccount")
    successMsg = (By.XPATH, "//p[contains(text(), 'Welcome to your account.')]")
    newsLetterChk = (By.NAME, "newsletter")
    offerChk = (By.NAME, "optin")
    countryNameTxt = (By.XPATH, "//div[@id='uniform-id_country']/span")

    def getCountryNameTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.countryNameTxt, interval=20)

    def getNewsLetterChk(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.newsLetterChk, interval=20)

    def getOfferChk(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.offerChk, interval=20)

    def getPersonalInformationLbl(self):
        return resuableFunctions.waitForElementVisible(self.driver, SignUpandInPage.personalInformationLbl, interval=20)

    def getMrRdBtn(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.mrRdBtn, interval=20)

    def getMrsRdBtn(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.mrsRdBtn, interval=20)

    def getCustFirstNameTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.custFirstNameTxt, interval=20)

    def getCustLastNameTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.custLastNameTxt, interval=20)

    def getEmailIDTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.emailIDTxt, interval=20)

    def getPasswordTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.passwordTxt, interval=20)

    def getDaysOpt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.daysOpt, interval=20)

    def getMonthOpt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.monthsOpt, interval=20)

    def getYearsOpt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.yearsOpt, interval=20)

    def getFirstNameTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.firstNameTxt, interval=20)

    def getLastNameTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.lastNameTxt, interval=20)

    def getCompanyTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.companyTxt, interval=20)

    def getAddress1Txt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.address1Txt, interval=20)

    def getAddress2Txt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.address2Txt, interval=20)

    def getCityTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.cityTxt, interval=20)

    def getStateOpt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.stateOpt, interval=20)

    def getPostCodeTxt(self):
        return resuableFunctions.waitForElementVisible(self.driver, SignUpandInPage.postCodeTxt, interval=20)

    def getCountryOpt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.countryOpt, interval=20)

    def getAdditionalInfoTextArea(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.additionalInfoTextArea, interval=20)

    def getHomePhoneTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.homePhoneTxt, interval=20)

    def getMobilePhoneTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.mobilePhoneTxt, interval=20)

    def getAliasAddrTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.aliasAddrTxt, interval=20)

    def getSubmitBtn(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.submitBtn, interval=20)

    def getSuccessMsg(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.successMsg, interval=20)



    # Error Locators in Registration Page
    errorDetails = (By.XPATH, "//div[contains(@class,'alert alert-danger')]")
    atleastOnePhNumberError = (By.XPATH, "//li[contains(text(), 'You must register at least one phone number.')]")
    homePhoneNumberError = (By.XPATH, "//li[contains(text(),'is invalid.')]/b[contains(text(), 'phone')]")
    mobilePhoneNumberError = (By.XPATH, "//li[contains(text(), 'is invalid.')]/b[contains(text(), 'phone_mobile')]")
    lastNameRequiredError = (By.XPATH, "//li[contains(text(), 'is required.')]/b[contains(text(), 'lastname')]")
    firstNameRequiredError = (By.XPATH, "//li[contains(text(), 'is required.')]/b[contains(text(), 'firstname')]")
    lastNameInvalidError = (By.XPATH, "//li[contains(text(), 'is invalid.')]/b[contains(text(), 'lastname')]")
    firstNameInvalidError = (By.XPATH, "//li[contains(text(), 'is invalid.')]/b[contains(text(), 'firstname')]")
    emailIdInvalidError = (By.XPATH, "//li[contains(text(), 'is invalid.')]/b[contains(text(), 'email')]")
    emailIdExistsError = (By.XPATH, "//li[contains(text(), 'An account using this')]")
    passwordRequiredError = (By.XPATH, "//li[contains(text(), 'is required.')]/b[contains(text(), 'passwd')]")
    passwordInvalidError = (By.XPATH, "//li[contains(text(), 'is invalid.')]/b[contains(text(), 'passwd')]")
    addressRequiredError = (By.XPATH, "//li[contains(text(), 'is required.')]/b[contains(text(), 'address1')]")
    cityRequiredError = (By.XPATH, "//li[contains(text(), 'is required.')]/b[contains(text(), 'city')]")
    countryRequiredError = (By.XPATH, "//li[contains(text(), 'is required.')]/b[contains(text(), 'id_country')]")
    countryInvalidError = (By.XPATH, "//li[contains(text(),'Country is invalid')]")
    countryLoadError = (By.XPATH, "//li[contains(text(),'Country cannot be loaded with address->id_country')]")
    aliasRequiredError = (By.XPATH, "//li[contains(text(), 'is required.')]/b[contains(text(), 'alias')]")
    stateRequiredError = (By.XPATH, "//li[contains(text(), 'This country requires you to choose a State.')]")
    postalCodeRequiredError = (By.XPATH, "//li[contains(text(),'It must follow this format: 00000')]")

    def getErrorDetails(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.errorDetails,
                                                        interval=20)

    def getAtleastOnePhNumberError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.atleastOnePhNumberError, interval=20)

    def getHomePhoneNumberError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.homePhoneNumberError, interval=20)

    def getMobilePhoneNumberError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.mobilePhoneNumberError, interval=20)

    def getLastNameRequiredError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.lastNameRequiredError, interval=20)

    def getFirstNameRequiredError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.firstNameRequiredError, interval=20)

    def getLastNameInvalidError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.lastNameInvalidError, interval=20)

    def getFirstNameInvalidError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.firstNameInvalidError, interval=20)

    def getEmailIdInvalidError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.emailIdInvalidError, interval=20)

    def getEmailIdExistsError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.emailIdExistsError, interval=20)

    def getPasswordRequiredError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.passwordRequiredError, interval=20)

    def getPasswordInvalidError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.passwordInvalidError, interval=20)

    def getAddressRequiredError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.addressRequiredError, interval=20)

    def getCityRequiredError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.cityRequiredError, interval=20)

    def getCountryRequiredError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.countryRequiredError, interval=20)

    def getCountryInvalidError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.countryInvalidError, interval=20)

    def getCountryLoadError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.countryLoadError, interval=20)

    def getCountryOpt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.countryOpt, interval=20)

    def getAdditionalInfoTextArea(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.additionalInfoTextArea,
                                                        interval=20)

    def getAliasRequiredError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.homePhoneTxt, interval=20)

    def getMobilePhoneTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.mobilePhoneTxt, interval=20)

    def getAliasAddrTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.aliasAddrTxt, interval=20)

    def getStateRequiredError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.stateRequiredError, interval=20)

    def getPostalCodeRequiredError(self):
        return resuableFunctions.waitForElementPresence(self.driver, SignUpandInPage.postalCodeRequiredError, interval=20)

#     An account using this email address has already been registered. Please enter a valid password or request a new one.
#     Invalid email address.
