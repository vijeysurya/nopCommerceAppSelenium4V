import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
ser_obj_chr=Service("/Users/vijeysurya/Drivers/chromedriver_mac64_m1/chromedriver")
ser_obj_fox=Service("/Users/vijeysurya/Drivers/geckodriver-v0.31.0-macos-aarch64/geckodriver 2")

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome(service=ser_obj_chr)
        print("Launching chrome browser")
    elif browser=="firefox":
        driver=webdriver.Firefox(service=ser_obj_fox)
        print("Launching firefox browser")
    else:
        driver=webdriver.Chrome(service=ser_obj_chr)
    return driver

def pytest_addoption(parser):#--this will enable the CLI for browser input
    parser.addoption("--browser")

@pytest.fixture()#--browser input will go to setup method
def browser(request):
    return request.config.getoption("--browser")

#---------------html reports-----------------#
def pytest_configure(config):#for adding environment info into HTML Reports
    config._metadata['Project Name']='nop commerce'
    config._metadata['Module Name']='Customer'
    config._metadata['Tester'] = 'VijeySuryaJ'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)






