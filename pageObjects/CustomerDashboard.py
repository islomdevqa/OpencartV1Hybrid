from selenium.webdriver.common.by import By


class CustomerDashboardPage:
    link_Logout_xpath = "//div[contains(text(),'Log out')]"

    def __init__(self, driver):
        self.driver = driver


    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_Logout_xpath).click()







