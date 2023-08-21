import time
from pageObjects.HomePage import HomePage
from pageObjects.CustomerLogin import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os
import pytest

class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    cus_email = ReadConfig.getUserEmail()
    cus_password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("*********  Starting test_002_CustomerLogin  ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickCustomers()
        self.hp.clickCustomerLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.cus_email)
        self.lp.setPassword(self.cus_password)
        self.lp.clickLogin()
        time.sleep(5)
        self.targetPage = self.lp.isCustomerDashboardExist()

        if self.targetPage == "Customer Profile":
            self.logger.info("Customer is successfully signed in the application!")
            screenshot_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
            screenshot_path = os.path.join(screenshot_folder, "customer_login_success.png")
            self.driver.save_screenshot(screenshot_path)
            time.sleep(3)
            self.driver.close()
            assert True
        else:
            self.logger.info("Customer is failed up the Login page!")
            screenshot_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
            screenshot_path = os.path.join(screenshot_folder, "customer_login_failed.png")
            if not os.path.exists(screenshot_folder):
                os.makedirs(screenshot_folder)
            self.driver.save_screenshot(screenshot_path)
            time.sleep(3)
            self.driver.close()
            assert False

        self.logger.info("***** test_002_CustomerLogin finished *****")




