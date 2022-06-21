from selenium.webdriver.common.by import By
import utilities.ReusableFunctions as resuableFunctions


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    productLnk = (By.XPATH, "(//div[@class='tab-content']//li[1]/div)[1]")
    productName = (By.XPATH, "//h1[@itemprop='name']")
    productPrice = (By.XPATH, "//div[@class='price']/p/span[@id='our_price_display']")
    sectionDataSheet = (By.XPATH, "//section[@class='page-product-box']/h3[text()='Data sheet']")
    sectionMoreInfo = (By.XPATH, "//section[@class='page-product-box']/h3[text()='More info']")
    sectionReviews = (By.XPATH, "//section[@class='page-product-box']/h3[text()='Reviews']")
    addToCart = (By.XPATH, "//p[@id='add_to_cart']//button[@type='submit']")
    addToCartLoading = (By.XPATH, "//button[@class='exclusive added disabled']")
    prdtAddedSuccessMsg = (By.XPATH, "//div[@class='clearfix']/div[contains(@class,'layer_cart_product')]/h2")
    proceedToChkOut = (By.XPATH, "//span[contains(text(),'Proceed to checkout')]")

    def getTitle(self):
        return resuableFunctions.getTitle(self.driver)

    def getProductLnk(self):
        return resuableFunctions.waitForElementPresence(self.driver, ProductPage.productLnk, interval=20)

    def getAddToCartLoading(self):
        return resuableFunctions.waitForElementNotPresent(self.driver, ProductPage.addToCartLoading, interval=20)

    def getProductName(self):
        return resuableFunctions.waitForElementPresence(self.driver, ProductPage.productName, interval=20)

    def getProductPrice(self):
        return resuableFunctions.waitForElementPresence(self.driver, ProductPage.productPrice, interval=20)

    def getSectionDataSheet(self):
        return resuableFunctions.waitForElementPresence(self.driver, ProductPage.sectionDataSheet, interval=20)

    def getSectionMoreInfo(self):
        return resuableFunctions.waitForElementPresence(self.driver, ProductPage.sectionMoreInfo, interval=20)

    def getSectionReviews(self):
        return resuableFunctions.waitForElementPresence(self.driver, ProductPage.sectionReviews, interval=20)

    def getAddToCart(self):
        return resuableFunctions.waitForElementPresence(self.driver, ProductPage.addToCart, interval=20)

    def getPrdtAddedSuccessMsg(self):
        return resuableFunctions.waitForElementVisible(self.driver, ProductPage.prdtAddedSuccessMsg, interval=1000)

    def getProceedToChkOut(self):
        return resuableFunctions.waitForElementPresence(self.driver, ProductPage.proceedToChkOut, interval=20)



