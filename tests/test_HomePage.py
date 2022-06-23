import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_formSubmission(self, getHomeData):
        log = self.getLogger()
        hompage = HomePage(self.driver)
        log.info("First Name is:"+getHomeData["firstname"])
        hompage.homeName().send_keys(getHomeData["firstname"])
        hompage.homeEmail().send_keys(getHomeData["email"])
        hompage.HomecheckBox().click()
        self.selectOptionByText(hompage.homeGenderDropDown(), getHomeData["gender"])
        hompage.homeSubmitButton().click()
        alertText = hompage.homeSuccessAlert().text
        print(alertText)
        assert "Success" in alertText
        self.driver.refresh()

    @pytest.fixture(params= HomePageData.test_homepage_data)

    def getHomeData(self, request):
        return request.param

