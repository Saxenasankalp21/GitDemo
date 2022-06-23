from selenium.webdriver.common.by import By

from PageObjects.CheckOutPage import CheckOutPage


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    productTitle = (By.XPATH, "//div[@class='card h-100']")
    productCheckout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    #driver.find_element(by=By.XPATH, value="//a[@class='nav-link btn btn-primary']")
    def getProductTitles(self):
        return self.driver.find_elements(*ShopPage.productTitle)

    def productCheckoutButton(self):
        self.driver.find_element(*ShopPage.productCheckout).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
