from selenium.webdriver.common.by import By


class LoginPage:
    txt_email_xpath = "//input[@id='input-13']"
    txt_password_xpath = "//input[@id='input-14']"
    click_SignIn_xpath = "//span[contains(text(),'Sign in')]"
    confirmation_CustomerDashboard_xpath = "//h3[contains(.,'Customer Profile')]"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.click_SignIn_xpath).click()

    def isCustomerDashboardExist(self):
        try:
            print(self.driver.find_element(By.XPATH, self.confirmation_CustomerDashboard_xpath).text)
            return self.driver.find_element(By.XPATH, self.confirmation_CustomerDashboard_xpath).text

        except:
            return None





