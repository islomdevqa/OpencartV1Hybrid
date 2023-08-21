from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:
    link_Customers_XPath = "//a[contains(.,'Customers')]"
    link_SignUp_XPath = "//a[contains(normalize-space(),'Sign Up')]"
    link_Login_XPath = "//a[contains(text(),'Login')]"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomers(self):
        self.driver.find_element(By.XPATH, self.link_Customers_XPath).click()

    def clickCustomerSignUp(self):
        self.driver.find_element(By.XPATH, self.link_SignUp_XPath).click()

    def clickCustomerLogin(self):
        self.driver.find_element(By.XPATH, self.link_Login_XPath).click()


















