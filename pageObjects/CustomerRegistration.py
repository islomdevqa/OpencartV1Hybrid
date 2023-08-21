from selenium.webdriver.common.by import By

class TestCustomerRegistration:
    txt_fname_XPath = "//input[contains(@id,'input-15')]"
    txt_lname_XPath = "//input[@id='input-16']"
    txt_email_XPath = "//input[@id='input-17']"
    txt_password_XPath = "//input[@id='input-18']"
    click_registerNow_xpath = "//span[normalize-space()='Register now']"
    # confirmation_SignIn_xpath = "//strong[contains(.,'Sign in')]"

    def __init__(self, driver):
        self.driver = driver

    def setFname(self, cus_fname):
        self.driver.find_element(By.XPATH, self.txt_fname_XPath).send_keys(cus_fname)

    def setLname(self, cus_lname):
        self.driver.find_element(By.XPATH, self.txt_lname_XPath).send_keys(cus_lname)

    def setEmail(self, cus_email):
        self.driver.find_element(By.XPATH, self.txt_email_XPath).send_keys(cus_email)

    def setPassword(self, cus_password):
        self.driver.find_element(By.XPATH, self.txt_password_XPath).send_keys(cus_password)

    def clickRegisterNowButton(self):
        self.driver.find_element(By.XPATH, self.click_registerNow_xpath).click()

    def getConfirmationMsg(self):
        try:
            return self.driver.current_url
        except:
            return False
