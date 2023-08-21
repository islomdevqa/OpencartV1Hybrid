import time
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.CustomerLogin import LoginPage
from pageObjects.CustomerDashboard import CustomerDashboardPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_Login_DDT:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    # Corrected path construction using your project structure
    path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "testData", "CLC-TestData.xlsx"))

    def test_login_ddt(self, setup):
        self.logger.info("******  Starting test_003_LoginDDT - Data Driven Testing  ******")

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")  # Corrected line

        lst_status = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = CustomerDashboardPage(self.driver)

        for r in range(2, self.rows + 1):
            self.hp.clickCustomers()
            self.hp.clickCustomerLogin()

            self.email = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            self.targetPage = self.lp.isCustomerDashboardExist()

            if self.exp == "Valid":
                if self.targetPage:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp == "Invalid":
                if self.targetPage:
                    lst_status.append("Fail")
                    self.ma.clickLogout()
                else:
                    lst_status.append("Pass")

        self.driver.close()

        if "Fail" not in lst_status:
            assert True
        else:
            assert False

        self.logger.info("******  End of test_003_LoginDDT - Data Driven Test  ******")
