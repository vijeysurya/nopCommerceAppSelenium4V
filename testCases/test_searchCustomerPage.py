import time

import pytest

from utilities.readProperties import ReadConfig
from utilities.cutomLogger import LogGen
from pageObjects.loginPage import Login
from pageObjects.addCustomerPage import AddCustomer
from  pageObjects.searchCustomerPage import SearchCustomer
class Test_SearchCustomer:
    baseurl=ReadConfig.getbaseurl()
    username=ReadConfig.getusername()
    password=ReadConfig.getpassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_004_searchcustomer_by_email(self,setup):
        self.logger.info("**** test_004_searchcustomer_by_email execution started ****")

        self.logger.info("**** Trying to login into application ****")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.lp.username_action(self.username)
        self.lp.password_action(self.password)
        self.lp.login_action()
        self.logger.info("**** Login Successful ****")

        self.logger.info("**** Search customer by email started ****")
        self.ac=AddCustomer(self.driver)
        self.ac.customermenu()
        time.sleep(30)
        self.ac.customersubmenu()
        self.sc=SearchCustomer(self.driver)
        self.sc.emailsearch("victoria_victoria@nopCommerce.com")
        self.sc.searchclick()
        time.sleep(5)
        status_email=self.sc.searchbyemail("victoria_victoria@nopCommerce.com")
        assert True==status_email
        self.logger.info("**** Search customer by email completed ****")

        self.logger.info("**** test_004_searchcustomer_by_email execution completed ****")
        time.sleep(3)
        self.driver.close()

    @pytest.mark.regression
    def test_005_searchcustomer_by_name(self,setup):
        self.logger.info("**** test_005_searchcustomer_by_name execution started ****")

        self.logger.info("**** Trying to login into application ****")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.lp.username_action(self.username)
        self.lp.password_action(self.password)
        self.lp.login_action()
        self.logger.info("**** Login Successful ****")

        self.logger.info("**** Search customer by name started ****")
        self.ac=AddCustomer(self.driver)
        self.ac.customermenu()
        time.sleep(30)
        self.ac.customersubmenu()
        self.sc=SearchCustomer(self.driver)
        self.sc.fnamesearch("Victoria")
        self.sc.lnamesearch("Terces")
        self.sc.searchclick()
        time.sleep(5)

        status_name=self.sc.searchbyname("Victoria Terces")
        assert True==status_name
        self.logger.info("**** Search customer by name completed ****")

        self.logger.info("**** test_005_searchcustomer_by_name execution completed ****")
        time.sleep(3)
        self.driver.close()

















