from selenium.webdriver.common.by import By
import utilities.ReusableFunctions as resuableFunctions


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    cartLnk = (By.XPATH, "//div[@class='shopping_cart']/a")
    shoppingCartSummaryTxt = (By.XPATH, "//h1[contains(text(), 'Shopping-cart summary')]")
    deleteItemLnk = (By.XPATH, "(//table[@id='cart_summary']/tbody/tr/td[@data-title='Delete']//a[@title='Delete'])[1]")
    productDetail = (By.XPATH, "(//table[@id='cart_summary']/tbody/tr)[1]")
    cartEmpty = (By.XPATH, "//p[contains(text(), 'Your shopping cart is empty.')]")

    def getCartLnk(self):
        return resuableFunctions.waitForElementPresence(self.driver, CartPage.cartLnk, interval=20)

    def getShoppingCartSummaryTxt(self):
        return resuableFunctions.waitForElementPresence(self.driver, CartPage.shoppingCartSummaryTxt, interval=20)

    def getDeleteItemLnk(self):
        return resuableFunctions.waitForElementPresence(self.driver, CartPage.deleteItemLnk, interval=20)

    def getCartEmpty(self):
        return resuableFunctions.waitForElementVisible(self.driver, CartPage.cartEmpty, interval=20)

    def getProductDetail(self):
        return resuableFunctions.waitForElementPresence(self.driver, CartPage.productDetail, interval=20)

