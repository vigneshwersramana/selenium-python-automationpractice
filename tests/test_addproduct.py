"""
This script is responsible for validating add a product funcnality
"""

# pylint: disable = R0801, E1101, C0103, C0116, C0301, C0115

import pytest
from loguru import logger

import utilities.ReusableFunctions as reusableFunctions
from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage
from pageObjects.SignInPage import SignUpandInPage
from utilities.Actions import Actions
from utilities.Base import Base


class Test_AddProduct(Base):

    @pytest.mark.add_product
    @pytest.mark.addfirstproduct
    @pytest.mark.positive
    def test_add_first_product(self, dataLoad):
        log = logger
        home = HomePage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)
        signIn = SignUpandInPage(self.driver)
        actions = Actions(self.driver)

        data = reusableFunctions.getTestCaseData(dataLoad, "TC10")

        home.getTitle()
        reusableFunctions.isTitle(home.getTitle(), "My Store")
        actions.click(home.getSignInBtn())
        log.info("Clicked on Sign In Button")

        actions.click(signIn.getEmailIdTxt())
        actions.sendKeys(signIn.getEmailIdTxt(), data.get("emailid"))
        actions.click(signIn.getPwdTxt())
        actions.sendKeys(signIn.getPwdTxt(), data.get("password"))
        actions.click(signIn.getSignInBtn())
        text = actions.getText(signIn.getMyAccountLbl())

        reusableFunctions.isText(text, "MY ACCOUNT")
        log.info("Login successful")

        actions.click(signIn.getHomePageLogo())

        reusableFunctions.isDisplayed(home.getWomenLnk(), "Women Section Link")
        reusableFunctions.isDisplayed(home.getDressesLnk(), "Dresses Section Link")
        reusableFunctions.isDisplayed(home.getTShirtsLink(), "TShirts Section Link")

        reusableFunctions.containsText(actions.getText(home.getProduct1Name()), data.get("productname"))
        reusableFunctions.containsText(actions.getText(home.getProduct1Price()), data.get("price"))
        actions.click(home.getProduct1Lnk())

        reusableFunctions.isTitle(product.getTitle(), "Faded Short Sleeve T-shirts - My Store")
        reusableFunctions.isDisplayed(product.getProductName(), "Product")
        reusableFunctions.isText(actions.getText(product.getProductName()), data.get("productname"))
        reusableFunctions.containsText(actions.getText(product.getProductPrice()), data.get("price"))

        actions.click(product.getAddToCart())

        reusableFunctions.isDisplayed(product.getSectionMoreInfo(), "More Info")
        reusableFunctions.isDisplayed(product.getSectionDataSheet(), "Data Sheet")
        reusableFunctions.isDisplayed(product.getSectionReviews(), "Reviews")
        #reusableFunctions.isDisplayed(product.getAddToCartLoading(), "Cart Loading")
        product.getAddToCartLoading()
        reusableFunctions.isDisplayed(product.getPrdtAddedSuccessMsg(), "Product successfully added")
        actions.click(product.getProceedToChkOut())

        reusableFunctions.isDisplayed(cart.getShoppingCartSummaryTxt(), "Cart Summary Page")
        reusableFunctions.isDisplayed(cart.getProductDetail(), "Product Detail")


    @pytest.mark.add_product
    @pytest.mark.addproduct_byname
    def test_add_product_by_name(self, dataLoad):
        log = logger
        home = HomePage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)
        signIn = SignUpandInPage(self.driver)
        actions = Actions(self.driver)

        data = reusableFunctions.getTestCaseData(dataLoad, "TC9")

        home.getTitle()
        reusableFunctions.isTitle(home.getTitle(), "My Store")
        actions.click(home.getSignInBtn())
        log.info("Clicked on Sign In Button")

        actions.click(signIn.getEmailIdTxt())
        actions.sendKeys(signIn.getEmailIdTxt(), data.get("emailid"))
        actions.click(signIn.getPwdTxt())
        actions.sendKeys(signIn.getPwdTxt(), data.get("password"))
        actions.click(signIn.getSignInBtn())
        text = actions.getText(signIn.getMyAccountLbl())

        reusableFunctions.isText(text, "MY ACCOUNT")
        log.info("Login successful")

        actions.click(signIn.getHomePageLogo())

        reusableFunctions.isDisplayed(home.getWomenLnk(), "Women Section Link")
        reusableFunctions.isDisplayed(home.getDressesLnk(), "Dresses Section Link")
        reusableFunctions.isDisplayed(home.getTShirtsLink(), "TShirts Section Link")

        productName, productPrice = home.createProductUnqName(data.get("productname"))
        reusableFunctions.containsText(actions.getText(productPrice), data.get("price"))
        actions.click(productName)

        reusableFunctions.containsText(product.getTitle(), data.get("productname"))
        reusableFunctions.isDisplayed(product.getProductName(), "Product")
        reusableFunctions.isText(actions.getText(product.getProductName()), data.get("productname"))
        reusableFunctions.containsText(actions.getText(product.getProductPrice()), data.get("price"))

        actions.click(product.getAddToCart())

        reusableFunctions.isDisplayed(product.getSectionMoreInfo(), "More Info")
        reusableFunctions.isDisplayed(product.getSectionDataSheet(), "Data Sheet")
        reusableFunctions.isDisplayed(product.getSectionReviews(), "Reviews")
        # reusableFunctions.isDisplayed(product.getAddToCartLoading(), "Cart Loading")
        product.getAddToCartLoading()
        reusableFunctions.isDisplayed(product.getPrdtAddedSuccessMsg(), "Product successfully added")
        actions.click(product.getProceedToChkOut())

        reusableFunctions.isDisplayed(cart.getShoppingCartSummaryTxt(), "Cart Summary Page")
        reusableFunctions.isDisplayed(cart.getProductDetail(), "Product Detail")
