import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddCustomer:
    lnk_customermenu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_customersubmenu_xpath="//li[@class='nav-item']/a[@class='nav-link']//p[text()=' Customers']"
    lnk_addnew_xpath="//a[@class='btn btn-primary']"
    txt_email_xpath="//input[@id='Email']"
    txt_password_xpath="//input[@id='Password']"
    txt_firstname_xpath="//input[@id='FirstName']"
    txt_lastname_xpath="//input[@id='LastName']"
    rd_gdrmale_xpath="//input[@id='Gender_Male']"
    rd_gdrfemale_xpath="//input[@id='Gender_Female']"
    txt_dateofbirth_id="DateOfBirth"
    txt_companyname_id="Company"
    rd_txaexempt_id="IsTaxExempt"
    lst_customerroles_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lst_customerroles_administartor_xpath="//li[normalize-space()='Administrators']"
    lst_customerroles_moderator_xpath="//li[normalize-space()='Forum Moderators']"
    lst_customerroles_guest_xpath="//li[normalize-space()='Guests']"
    lst_customerroles_registered_xpath="//li[contains(text(),'Registered')]"
    lst_customerroles_vendors_xpath="//li[contains(text(),'Vendors')]"
    drp_mgrvendor_xpath="//select[@id='VendorId']"
    txt_admincontent_xpath="//textarea[@id='AdminComment']"
    btn_save_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def customermenu(self):
        self.driver.find_element(By.XPATH,self.lnk_customermenu_xpath).click()

    def customersubmenu(self):
        self.driver.find_element(By.XPATH,self.lnk_customersubmenu_xpath).click()

    def addnew(self):
        self.driver.find_element(By.XPATH,self.lnk_addnew_xpath).click()

    def email(self,email_in):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email_in)

    def password(self,password_in):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(password_in)

    def firstname(self,firstname_in):
        self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(firstname_in)

    def lastname(self,lastname_in):
        self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(lastname_in)

    def gender(self,gender_in):
        if gender_in=="Male":
            self.driver.find_element(By.XPATH,self.rd_gdrmale_xpath).click()
        elif gender_in=="Female":
            self.driver.find_element(By.XPATH,self.rd_gdrfemale_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_gdrmale_xpath).click()

    def dateofbirth(self,dateofbirth_in):
        self.driver.find_element(By.ID,self.txt_dateofbirth_id).send_keys(dateofbirth_in)

    def companyname(self,companyname_in):
        self.driver.find_element(By.ID,self.txt_companyname_id).send_keys(companyname_in)

    def taxexempt(self):
        tax_exempt_clk=self.driver.find_element(By.ID,self.rd_txaexempt_id)
        if tax_exempt_clk.is_selected():
            None
        else:
            tax_exempt_clk.click()

    def customerroles(self,customerroles_in):
        listitem=self.driver.find_element(By.XPATH,self.lst_customerroles_xpath)
        if customerroles_in=="Administrator":
            listitem.click()
            self.list_item=self.driver.find_element(By.XPATH,self.lst_customerroles_administartor_xpath)
        elif customerroles_in=="Moderator":
            listitem.click()
            self.list_item=self.driver.find_element(By.XPATH,self.lst_customerroles_moderator_xpath)
        elif customerroles_in=="Vendor":
            listitem.click()
            self.list_item=self.driver.find_element(By.XPATH,self.lst_customerroles_vendors_xpath)
        elif customerroles_in=="Guest":
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            time.sleep(6)
            listitem.click()
            time.sleep(5)
            self.list_item=self.driver.find_element(By.XPATH,self.lst_customerroles_guest_xpath)
        elif customerroles_in=="Registered":
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            time.sleep(6)
            listitem.click()
            time.sleep(5)
            self.list_item = self.driver.find_element(By.XPATH, self.lst_customerroles_registered_xpath)
        else:
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            time.sleep(6)
            listitem.click()
            time.sleep(5)
            self.list_item = self.driver.find_element(By.XPATH, self.lst_customerroles_guest_xpath)
        #self.list_item.click()#this wont work since list item item cant be clickable by clickaction
        #for the workaround we have to use javascript .execute_script action
        self.driver.execute_script("arguments[0].click();",self.list_item)
        # time.sleep(10)

    def mgrvendor(self,mgrvendor_in):
        drop_mgr=Select(self.driver.find_element(By.XPATH,self.drp_mgrvendor_xpath))
        drop_mgr.select_by_visible_text(mgrvendor_in)

    def admincontent(self,admincontent_in):
        self.driver.find_element(By.XPATH,self.txt_admincontent_xpath).send_keys(admincontent_in)

    def save(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()


















