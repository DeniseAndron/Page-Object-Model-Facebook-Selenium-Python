from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import sys
sys.path.append("C://Users/Denisa\Desktop/selenium/facebook")


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
    click_on_profile_page = (By.XPATH, '//div[@id="u_0_a"]/div[1]/div[1]/div')

    def __init__(self, driver):
        self.driver = driver

    def goToProfile(self):
        self.driver.find_element(self.click_on_profile_page).click()

