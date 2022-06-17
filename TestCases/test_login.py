import time

from PageObjects.LoginPage import Login


class Test_Login_TC001:
    url = "https://opensource-demo.orangehrmlive.com/"
    def test_loginpage(self, driver):
        driver.get(self.url)
        title = driver.title
        print("TITLE IS: ", title)

        if title == "OrangeHRM":
            driver.close()
            assert True
        else:
            driver.save_screenshot(".\\ScreenShots\\test_loginpage.png")
            driver.close()
            assert False

    def test_ValidLogin(self, driver):
        user = "Admin"
        password = "admin123"
        driver.get(self.url)
        self.loginPageobjects = Login(driver)
        self.loginPageobjects.setUserName(user)
        self.loginPageobjects.setPasswd(password)
        self.loginPageobjects.clickLogin()
        title = self.loginPageobjects.getDashboardText()
        print("TITLE IS: ", title)

        if title == "Dashboard":
            driver.close()
            assert True
        else:
            driver.save_screenshot(".\\ScreenShots\\test_ValidLogin.png")
            driver.close()
            assert False

    def test_WithoutCredentials(self, driver):
        driver.get(self.url)
        self.loginPageobjects = Login(driver)
        self.loginPageobjects.clickLogin()
        message = self.loginPageobjects.getMessageText()

        if message == "Username cannot be empty":
            driver.close()
            assert True
        else:
            driver.save_screenshot(".\\ScreenShots\\test_WithoutCredentials.png")
            driver.close()
            assert False

    def test_EmptyPassword(self, driver):
        user = "Admin"
        driver.get(self.url)
        self.loginPageobjects = Login(driver)
        self.loginPageobjects.setUserName(user)
        time.sleep(3)
        self.loginPageobjects.clickLogin()
        time.sleep(3)
        message = self.loginPageobjects.getMessageText()

        if message == "Password cannot be empty":
            driver.close()
            assert True
        else:
            driver.save_screenshot(".\\ScreenShots\\test_EmptyPassword.png")
            driver.close()
            assert False

    def test_InvalidLogin(self, driver):
        user = "Admin"
        password = "admin12"
        driver.get(self.url)
        self.loginPageobjects = Login(driver)
        self.loginPageobjects.setUserName(user)
        self.loginPageobjects.setPasswd(password)
        self.loginPageobjects.clickLogin()
        message = self.loginPageobjects.getMessageText()

        if message == "Invalid credentials":
            driver.close()
            assert True
        else:
            driver.save_screenshot(".\\ScreenShots\\test_InvalidLogin.png")
            driver.close()
            assert False