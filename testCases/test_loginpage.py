import pytest

from pageObjects.loginPage import Login
from utilities.readProperties import ReadConfig
from utilities.cutomLogger import LogGen

class Test_login:
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    baseurl = ReadConfig.getbaseurl()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_tc001_homepage_title(self, setup):
        self.logger.info("****test_tc001_homepage_title started****")
        self.driver = setup
        self.driver.get(self.baseurl)
        home_act_title = self.driver.title
        self.logger.info("****Verifying the homepage title****")
        if home_act_title == "Your store. Login":
            self.logger.info("****Homepage title matched and passed****")
            assert True
            self.driver.close()
        else:
            self.logger.error("****Homepage title mismatched and failed****")
            self.driver.save_screenshot("/Users/vijeysurya/PycharmProjects/pythonProject1/nopCommerceAppSelenium4V/Screenshots/test_tc001_homepage_title.png")
            self.driver.close()
            assert False
        self.logger.info("****test_tc001_homepage_title completed****")

    @pytest.mark.sanity
    def test_tc002_login(self, setup):
        self.logger.info("****test_tc002_login started****")
        self.driver = setup
        self.driver.get(self.baseurl)
        lp=Login(self.driver)
        lp.username_action(self.username)
        lp.password_action(self.password)
        lp.login_action()
        self.logger.info("****Verifying the loginpage title****")
        login_act_title = self.driver.title
        if login_act_title == "Dashboard / nopCommerce administration":
            self.logger.info("****Loginpage title matched and passed****")
            assert True
            self.driver.close()
        else:
            self.logger.error("****Loginpage title mismatched and failed****")
            self.driver.save_screenshot("/Users/vijeysurya/PycharmProjects/pythonProject1/nopCommerceAppSelenium4V/Screenshots/test_tc002_login.png")
            self.driver.close()
            assert False
        self.logger.info("****test_tc002_login completed****")










