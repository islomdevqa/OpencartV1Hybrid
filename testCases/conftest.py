import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome": #Chrome is not working due to not available matching version with Chrome browser (114-116v)
        serv_obj=Service("C:/Users/islomdev/Downloads/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    elif browser == "edge":
        serv_obj = Service("C:/Users/islomdev/Documents/edgedriver_win64/msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)
    else:
        serv_obj = Service("C:/Users/islomdev/Downloads/geckodriver-v0.33.0-win64/geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# ----------------  pytest HTML Reports  ------------------


# def pytest_configure(config):
#     config._metadata["Project name"] = "TopHelpers"
#     config.option.module_name = "Login Module"
#     config.option.tester = "Islombek"
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Java home", None)
#     metadata.pop("Plugins", None)

# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     reports_folder = os.path.abspath(os.path.join(os.curdir, "..", "reports"))
#     config.option.htmlpath = os.path.join(reports_folder, datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html")

def pytest_configure(config):
    reports_folder = os.path.abspath(os.path.join(os.curdir, "reports"))
    config.option.htmlpath = os.path.join(reports_folder, datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html")

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    if not os.path.exists("reports"):
        os.makedirs("reports")
    if os.path.exists(session.config.option.htmlpath):
        new_path = os.path.join("reports", os.path.basename(session.config.option.htmlpath))
        os.rename(session.config.option.htmlpath, new_path)












