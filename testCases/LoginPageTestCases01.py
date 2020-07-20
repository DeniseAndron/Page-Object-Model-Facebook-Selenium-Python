
import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys

sys.path.append("C://Users/Denisa/Desktop/selenium/facebook")
from pageObjects.LogInPage import LoginPage
from Resources.TestData import TestData
from pageObjects.ContentPage import contentPageFacebook
from testCases.BaseTest import facebookTestBase


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


    def test_08_errorMessage(self):
        lp = LoginPage(self.driver)
        lp.checkLogin()

    def test_09_clickProfile(self):
        cp = contentPageFacebook(self.driver)
        cp.goToProfile()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner (output="C:\\Users\\Denisa\\Desktop\\selenium\\facebook\\reports"))