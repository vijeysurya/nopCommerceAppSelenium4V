import string
import random
import time

import pytest
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.cutomLogger import LogGen
from pageObjects.loginPage import Login
from pageObjects.addCustomerPage import AddCustomer



class Test_AddCutomer:
    baseurl=ReadConfig.getbaseurl()
    username=ReadConfig.getusername()
    password=ReadConfig.getpassword()
    logger=LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_tc003_addcustomer(self, setup):
        self.logger.info("****test_tc003_addcustomer started****")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        lp=Login(self.driver)
        self.logger.info("****Trying to Login****")
        lp.username_action(self.username)
        lp.password_action(self.password)
        lp.login_action()
        self.logger.info("****Login successful****")

        self.logger.info("****Add customer test started****")
        ac=AddCustomer(self.driver)
        ac.customermenu()
        time.sleep(30)
        ac.customersubmenu()
        ac.addnew()

        self.logger.info("****Proving customer info****")
        self.email_rd=random_generator() + "@gmail.com"
        ac.email(self.email_rd)
        ac.password("Changeme123")
        ac.firstname("Vijey")
        ac.lastname("SuryaJ")
        ac.gender("Male")
        ac.dateofbirth("09/05/1997")
        ac.companyname("Tata Consultancy Services")
        ac.taxexempt()
        ac.customerroles("Moderator")
        ac.mgrvendor("Vendor 2")
        ac.admincontent("Critical Customer")

        self.logger.info("****Proving customer info completed****")

        self.logger.info("****Saving customer info started****")
        ac.save()
        self.logger.info("****Saving customer info completed****")

        self.logger.info("****Add customer validation started****")
        self.savemessage=self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissable']").text
        print(self.savemessage)
        if 'The new customer has been added successfully.' in self.savemessage:
            self.logger.info("****Add customer test passed****")
            assert True == True
        else:
            self.driver.save_screenshot("/Users/vijeysurya/PycharmProjects/pythonProject1/nopCommerceAppSelenium4V/Screenshots/test_tc003_addcustomer.png")
            self.logger.error("****Add customer test failed****")
            assert True == False
        self.logger.info("****Add customer validation completed****")

        time.sleep(10)
        self.driver.close()
        self.logger.info("****test_tc003_addcustomer started****")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

