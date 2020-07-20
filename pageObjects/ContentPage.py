from selenium.webdriver.support.ui import Select
import sys
sys.path.append("C://Users/Denisa\Desktop/selenium/facebook")
from Resources.locators import *

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

class contentPageFacebook():
    def __init__(self, driver):
        self.driver = driver

    def goToProfile(self):
        self.driver.find_element(*MainPageLocators.click_on_profile_page).click()

