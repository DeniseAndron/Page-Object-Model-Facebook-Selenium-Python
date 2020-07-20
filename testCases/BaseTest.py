import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys

sys.path.append("C://Users/Denisa/Desktop/selenium/facebook")
from pageObjects.LogInPage import LoginPage
from pageObjects.SignUpPage import SignUpPage
from Resources.TestData import TestData
from pageObjects.ContentPage import contentPageFacebook


class facebookTestBase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        #disable the pop-up notifications
        chrome_options.add_argument("--disable-notifications")

        cls.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH, options=chrome_options)
        cls.driver.get(TestData.baseURL)
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        cls.driver.delete_all_cookies()
        cls.driver.close()





    #login

class LogInTestContent(facebookTestBase):
    @classmethod
    def setUpClass(cls):
        # to call the setUp() method of base class or super class.
        super().setUpClass()

    def test_05_LoginUsername(self):
        lp = LoginPage(self.driver)
        lp.setUsername(TestData.username)

    def test_06_LoginPassword(self):
        lp = LoginPage(self.driver)
        lp.setLoginPassword(TestData.loginPassword)

    def test_07_loginButton(self):
        lp = LoginPage(self.driver)
        lp.setButtonLogin()
        time.sleep(5)

    def test_08_errorMessage(self):
        lp = LoginPage(self.driver)
        lp.checkLogin()

    def test_09_clickProfile(self):
        cp = contentPageFacebook(self.driver)
        cp.goToProfile()





if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner (output="C:\\Users\\Denisa\\Desktop\\selenium\\facebook\\reports"))