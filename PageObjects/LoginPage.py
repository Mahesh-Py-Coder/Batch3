from selenium.webdriver.common.by import By


class Login:
    username_id = "txtUsername"
    passwd_id = "txtPassword"
    login_button_id = "btnLogin"
    message_id = "spanMessage"
    drop_down_id = "welcome"
    dashboard_xpath = '//div[@class="head"]/h1'
    logout_button_xpath = '//*[@id="welcome-menu"]/ul/li[3]/a'

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def setPasswd(self, passwd):
        self.driver.find_element(By.ID, self.passwd_id).clear()
        self.driver.find_element(By.ID, self.passwd_id).send_keys(passwd)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.login_button_id).click()

    def getMessageText(self):
        message = self.driver.find_element(By.ID, self.message_id)
        return message.text

    def clickDropDown(self):
        self.driver.find_element(By.ID, self.drop_down_id).click()

    def getDashboardText(self):
        elem = self.driver.find_element(By.XPATH, self.dashboard_xpath)
        return elem.text
