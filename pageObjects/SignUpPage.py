from selenium.webdriver.support.ui import Select
import sys
sys.path.append("C://Users/Denisa\Desktop/selenium/facebook")
from Resources.locators import *

class SignUpPage():


    #create one constructor to initialize the driver to indentify the elements

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, firstname):
        self.driver.find_element(*MainPageLocators.first_name_xpath).send_keys(firstname)

    def setSurname(self, surname):
        self.driver.find_element(*MainPageLocators.surname_xpath).send_keys(surname)

    def setEmail (self, email):
        self.driver.find_element(*MainPageLocators.email_xpath).send_keys(email)

    def setSecondEmail(self, secondEmail):
        self.driver.find_element(*MainPageLocators.c_email_xpath).send_keys(secondEmail)

    def setPassword(self, password):
        self.driver.find_element(*MainPageLocators.password_xpath).send_keys(password)

    #Pick your birthday

    def birthdayDay(self,daySelect):
        Select(self.driver.find_element(*MainPageLocators.day)).select_by_index(daySelect)

    def birthdayMonth(self, monthSelect):
        Select(self.driver.find_element(*MainPageLocators.month)).select_by_index(monthSelect)

    def birthdayYear(self, yearSelect):
        Select(self.driver.find_element(*MainPageLocators.year)).select_by_visible_text(yearSelect)

    def genderFemale(self):

        gender = self.driver.find_element(*MainPageLocators.female)

        # check if the female gender is selected and print the result, should be false
        verify_gender = gender.is_selected()
        print("The female button is selected " + str(verify_gender))

        # if the gender is not selected, click on it
        if verify_gender != True:
            gender.click()
        #check if the button is selected and print the result, should be true
        verify_gender = gender.is_selected()
        print("The female button is selected " + str(verify_gender))

    def genderMale(self):

        gender = self.driver.find_element(*MainPageLocators.male)

        # check if the male gender is selected and print the result, should be false
        verify_gender = gender.is_selected()
        print("The male button is selected " + str(verify_gender))

        # if the gender is not selected, click on it
        if verify_gender != True:
            gender.click()
        # check if the button is selected and print the result, should be true
        verify_gender = gender.is_selected()
        print("The male button is selected " + str(verify_gender))

    def genderCustom(self):

        gender = self.driver.find_element(*MainPageLocators.custom)

        # check if the custom gender is selected and print the result, should be false
        verify_gender = gender.is_selected()
        print("The custom button is selected " + str(verify_gender))

        # if the gender is not selected, click on it
        if verify_gender != True:
            gender.click()
        # check if the button is selected and print the result, should be true
        verify_gender = gender.is_selected()
        print("The custom button is selected " + str(verify_gender))

    def pronounSelect(self, pronounCheck):
        Select(self.driver.find_element(*MainPageLocators.pronoun)).select_by_value(pronounCheck)

    def optionalGenderInput(self, genderOptional):
        self.driver.find_element(*MainPageLocators.genderOptional_xpath).send_keys(genderOptional)




    #def genderCustom(self):
     #  verify_gender = self.driver.find_element(*MainPageLocators.female).is_selected()
      #  if verify_gender != True:
      #      verify_gender.click()
