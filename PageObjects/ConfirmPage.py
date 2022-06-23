from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    #country = (By.XPATH, "//a[text()='India']")  # This is to explicit wait for country
    deliveryCountry = (By.ID, "country")
    selectcountry = (By.XPATH, "//a[text()='India']")
    checkbox = (By.XPATH, "//label[@for='checkbox2']")
    submitbutton = (By.XPATH, "//input[@type='submit']")
    successmessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def countryDropDown(self):
        return self.driver.find_element(*ConfirmPage.deliveryCountry)

    def selectCountry(self):
        return self.driver.find_element(*ConfirmPage.selectcountry)

    def selectCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def submitButton(self):
        return self.driver.find_element(*ConfirmPage.submitbutton)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successmessage)
