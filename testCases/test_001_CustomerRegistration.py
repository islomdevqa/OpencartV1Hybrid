import time
from pageObjects.HomePage import HomePage
from pageObjects.CustomerRegistration import TestCustomerRegistration
from utilities import randomeString
import os
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_CustomerReg:
    # baseUrl = "https://test.tophelpers.techcells.one/"
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_customer_reg(self, setup):
        self.logger.info("***** test_001_CustomerRegistration launched *****")
        self.driver = setup
        self.logger.info("Application is opened!!")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("Clicking on customer registration button")
        self.hp.clickCustomers()
        self.hp.clickCustomerSignUp()

        self.regpage = TestCustomerRegistration(self.driver)
        self.logger.info("--- Entering customer details into fields ---")
        self.regpage.setFname("Islom")
        self.regpage.setLname("Kinsma")
        # self.regpage.setEmail("loreddffdso35")
        self.email = randomeString.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setPassword("islomdev")
        time.sleep(2)
        self.regpage.clickRegisterNowButton()
        time.sleep(5)
        self.confmsg = self.regpage.getConfirmationMsg()
        time.sleep(5)
        if self.confmsg == "https://dashboard.test.tophelpers.techcells.one/login":
            self.logger.info("Customer is successfully registered from the application!")
            screenshot_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
            screenshot_path = os.path.join(screenshot_folder, "customer_register_success.png")
            self.driver.save_screenshot(screenshot_path)
            assert True
        else:
            self.logger.info("Customer is failed up the Customer Registration page!")
            screenshot_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
            screenshot_path = os.path.join(screenshot_folder, "customer_register_failed.png")

            if not os.path.exists(screenshot_folder):
                os.makedirs(screenshot_folder)

            self.driver.save_screenshot(screenshot_path)
            assert False
        self.driver.close()
        self.logger.info("***** test_001_CustomerRegistration finished *****")




