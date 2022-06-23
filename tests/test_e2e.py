import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage


class TestOne(BaseClass):
    def test_e2e(self):
        self.driver.implicitly_wait(3)
        log = self.getLogger()
        Homepage = HomePage(self.driver)
        shopPage = Homepage.shopItems()
        log.info("Getting all the shop items")
        products = shopPage.getProductTitles()
        for product in products:
            item = product.find_element(by=By.XPATH, value="div/h4/a").text
            log.info(item)
            if item == "Blackberry":
                product.find_element(by=By.XPATH, value="div/button[@class='btn btn-info']").click()
        checkOutPage = shopPage.productCheckoutButton()
        final_checkout = checkOutPage.getProductTitleCheckout()
        if final_checkout.text == "Blackberry":
            confirmPage = checkOutPage.checkOutButton()
        else:
            log.info("The product in checkout page is different")
        confirmPage.countryDropDown().send_keys("ind")
        self.verifyDropDownLinkPresence("India")
        confirmPage.selectCountry().click()
        confirmPage.selectCheckbox().click()
        confirmPage.submitButton().click()
        success = confirmPage.getSuccessMessage()
        log.info(success.text)
        assert "Success!" in success.text
