from selenium.webdriver.common.by import By

from PageObjects.ShopPage import ShopPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    genderdropdwon = (By.ID, "exampleFormControlSelect1")
    homesubmit = (By.XPATH, "//input[@value='Submit']")
    homesuccessalert = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        shopPage = ShopPage(self.driver)
        return shopPage

    def homeName(self):
        return self.driver.find_element(*HomePage.name)

    def homeEmail(self):
        return self.driver.find_element(*HomePage.email)

    def HomecheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def homeGenderDropDown(self):
        return self.driver.find_element(*HomePage.genderdropdwon)

    def homeSubmitButton(self):
        return self.driver.find_element(*HomePage.homesubmit)

    def homeSuccessAlert(self):
        return self.driver.find_element(*HomePage.homesuccessalert)
