from selenium.webdriver.common.by import By


class SearchCustomer:
    txt_email_id="SearchEmail"
    txt_fname_id="SearchFirstName"
    txt_lname_id="SearchLastName"
    btn_search_id="search-customers"

    tbl_table_xpath="//table[@id='customers-grid']"
    tbl_getrows_xpath="//table[@id='customers-grid']//tbody/tr"
    tbl_getcolumns_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def emailsearch(self,email_in):
        self.driver.find_element(By.ID,self.txt_email_id).send_keys(email_in)

    def fnamesearch(self,fname_in):
        self.driver.find_element(By.ID, self.txt_fname_id).clear()
        self.driver.find_element(By.ID,self.txt_fname_id).send_keys(fname_in)

    def lnamesearch(self,lname_in):
        self.driver.find_element(By.ID, self.txt_lname_id).clear()
        self.driver.find_element(By.ID,self.txt_lname_id).send_keys(lname_in)

    def searchclick(self):
        self.driver.find_element(By.ID,self.btn_search_id).click()

    def getrowcount(self):
        return len(self.driver.find_elements(By.XPATH,self.tbl_getrows_xpath))

    def getcolumncount(self):
        return len(self.driver.find_elements(By.XPATH,self.tbl_getcolumns_xpath))

    def searchbyemail(self,email_in):
        flag=False
        for r in range(1,self.getrowcount()+1):
            table=self.driver.find_element(By.XPATH,self.tbl_table_xpath)
            email_id=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if email_id==email_in:
                flag=True
                break
        return flag

    def searchbyname(self,Name):
        flag=False
        for r in range(1,self.getrowcount()+1):
            table=self.driver.find_element(By.XPATH, self.tbl_table_xpath)
            name=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if Name==name:
                flag=True
                break
        return flag






