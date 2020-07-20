from selenium.common.exceptions import NoSuchElementException
import sys
sys.path.append("C://Users/Denisa\Desktop/selenium/facebook")
from Resources.locators import *
from pageObjects.Pages import BasePage
from Resources.TestData import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Test cases
#1. Login using the login page class -yes
#check if you are logged in -  yes
#post a message
#delete a post
#post a picture
#Tag people
#search for people
# add a friend
#delete a friend


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def setUsername(self, username):
        self.driver.find_element(*MainPageLocators.textbox_username_id).send_keys(username)

    def setLoginPassword(self):
        self.enter_text(*MainPageLocators.textbox_password_id, TestData.loginPassword)

    def setButtonLogin(self):
        self.click(MainPageLocators.button_login_id)

    #the test with run with success both times, you will now if you are logged in or if you are not
    def checkLogin(self):

        # modify this - assert at error message
        try:
            self.driver.find_element(*MainPageLocators.login_error_message)
            print('You are not logged in, wrong username or password')
        except NoSuchElementException:
            print('You are logged in')





