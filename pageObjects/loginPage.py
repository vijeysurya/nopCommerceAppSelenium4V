from selenium.webdriver.common.by import By


class Login:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//button[@type='submit']"
    button_logout_xpath="//a[normalize-space()='Logout']"
    def __init__(self,driver):
        self.driver=driver
    def username_action(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
    def password_action(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
    def login_action(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
    def logout_action(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()





