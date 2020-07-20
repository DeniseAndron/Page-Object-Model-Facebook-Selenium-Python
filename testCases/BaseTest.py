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


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner (output="C:\\Users\\Denisa\\Desktop\\selenium\\facebook\\reports"))