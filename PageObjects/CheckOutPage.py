from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    producttitle = (By.XPATH, "//a[text()='Blackberry']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")


    def getProductTitleCheckout(self):
        return self.driver.find_element(*CheckOutPage.producttitle)

    def checkOutButton(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
