import time

from pageObjects.loginPage import Login
from utilities.readProperties import ReadConfig
from utilities.cutomLogger import LogGen
from utilities import ExcelUtility

class Test_login:
    baseurl = ReadConfig.getbaseurl()
    file="/Users/vijeysurya/PycharmProjects/pythonProject1/nopCommerceAppSelenium4V/testData/LoginData.xlsx"
    logger=LogGen.loggen()
    list_status=[]
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

    def test_tc002_login(self, setup):
        self.logger.info("****test_tc002_login started****")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logger.info("****Getting row count****")
        self.rows=ExcelUtility.row_count(self.file,"Sheet1")
        self.logger.info("****For loop iteration started****")
        for r in range(2,self.rows+1):
            self.user=ExcelUtility.read_data(self.file,"Sheet1",r,1)
            self.pwd=ExcelUtility.read_data(self.file,"Sheet1",r,2)
            self.exp_status=ExcelUtility.read_data(self.file,"Sheet1",r,3)
            lp=Login(self.driver)
            lp.username_action(self.user)
            lp.password_action(self.pwd)
            lp.login_action()
            time.sleep(30)
            act_title=self.driver.title
            if act_title=="Dashboard / nopCommerce administration":
                if self.exp_status=="Pass":
                    self.logger.info("****Passed****")
                    lp.logout_action()
                    self.list_status.append("Pass")
                elif self.exp_status=="Fail":
                    self.logger.error("****Failed****")
                    lp.logout_action()
                    self.list_status.append("Fail")
            elif act_title!="Dashboard / nopCommerce administration":
                if self.exp_status=="Pass":
                    self.logger.error("****Failed****")
                    self.list_status.append("Fail")
                elif self.exp_status=="Fail":
                    self.logger.info("****Passed****")
                    self.list_status.append("Pass")
        self.logger.info("****For loop iteration completed****")
        if "Fail" not in self.list_status:
            self.logger.info("****Login DDT test passed****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login DDT test Failed****")
            self.driver.close()
            assert False
        self.logger.info("****test_tc002_login completed****")
















