from selenium.webdriver.common.by import By
import utilities.ReusableFunctions as resuableFunctions


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    signInBtn = (By.XPATH, "//a[contains(text(),'Sign in')]")
    womenLnk = (By.XPATH, "//a[text()='Women']")
    dressesLnk = (By.XPATH, "(//a[text()='Dresses'])[2]")
    tshirtsLnk = (By.XPATH, "(//a[text()='T-shirts'])[2]")
    cartLnk = (By.XPATH, "//div[@class='shopping_cart']/a")

    def getCartLnk(self):
        return resuableFunctions.waitForElementPresence(self.driver, HomePage.cartLnk, interval=20)

    def getSignInBtn(self):
        return resuableFunctions.waitForElementPresence(self.driver, HomePage.signInBtn, interval=20)

    def getWomenLnk(self):
        return resuableFunctions.waitForElementPresence(self.driver, HomePage.womenLnk, interval=20)

    def getDressesLnk(self):
        return resuableFunctions.waitForElementPresence(self.driver, HomePage.dressesLnk, interval=20)

    def getTShirtsLink(self):
        return resuableFunctions.waitForElementPresence(self.driver, HomePage.tshirtsLnk, interval=20)

    def getTitle(self):
        return resuableFunctions.getTitle(self.driver)

    product1Lnk = (By.XPATH, "(//div[@class='tab-content']//li[1]/div)[1]")
    product1Name = (By.XPATH, "(//div[@class='tab-content']//li[1]/div//h5/a)[1]")
    product1Price = (By.XPATH, "(//div[@class='right-block']/div[@class='content_price']/span)[1]")

    def getProduct1Lnk(self):
        return resuableFunctions.waitForElementPresence(self.driver, HomePage.product1Lnk, interval=20)

    def getProduct1Name(self):
        return resuableFunctions.waitForElementPresence(self.driver, HomePage.product1Name, interval=20)

    def getProduct1Price(self):
        return resuableFunctions.waitForElementPresence(self.driver, HomePage.product1Price, interval=20)

    def createProductUnqName(self, text):
        # (//a[contains(text(),'Faded Short Sleeve T-shirts')])[1]
        productUnqName = (By.XPATH, "(//a[contains(text(),'" + text + "')])[1]")
        productPrice = (By.XPATH,
                        "(//a[contains(text(),'" + text + "')]//parent::h5//parent::div/div/span)[1]")
        return resuableFunctions.waitTobeClickable(self.driver, productUnqName, interval=20), \
               resuableFunctions.waitForElementPresence(self.driver, productPrice, interval=20)

    def createProductUnqPrice(self, text):
        # (//div[@class='right-block']//span[@class='price product-price' and contains(text(), '')])[1]
        productUnqPrice = (By.XPATH,
                           "(//div[@class='right-block']//span[@class='price product-price' and contains(text(), '" + text + "')])[1]")
        return resuableFunctions.waitTobeClickable(self.driver, productUnqPrice, interval=20)
