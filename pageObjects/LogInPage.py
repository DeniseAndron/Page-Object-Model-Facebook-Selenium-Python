from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import sys
sys.path.append("C://Users/Denisa\Desktop/selenium/facebook")
from pageObjects.Pages import BasePage
from Resources.TestData import TestData





class LoginPage(BasePage):
    textbox_username_id = (By.ID, "email")
    textbox_password_id = (By.ID, "pass")
    button_login_id = (By.ID, "u_0_b")
    login_error_message = (By.XPATH, ".//div[@class='_5v-0 _53in']")



    def __init__(self, driver):
        super().__init__(driver)


    def setUsername(self, username):
        self.driver.find_element(*self.textbox_username_id).send_keys(username)

    def setLoginPassword(self, password):
        self.driver.find_element(*self.textbox_password_id).send_keys(password)

    def setButtonLogin(self):
        self.click(self.button_login_id)

    #the test with run with success both times, you will now if you are logged in or if you are not
    def checkLogin(self):

        # modify this - assert at error message
        try:
            self.driver.find_element(*self.login_error_message)
            print('You are not logged in, wrong username or password')
        except NoSuchElementException:
            print('You are logged in')





