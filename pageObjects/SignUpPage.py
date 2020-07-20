from selenium.webdriver.support.ui import Select
import sys
sys.path.append("C://Users/Denisa\Desktop/selenium/facebook")
from selenium.webdriver.common.by import By

class SignUpPage():
    first_name_xpath = (By.XPATH, '//input[@name="firstname"]')
    surname_xpath = (By.XPATH, '//input[@name="lastname"]')
    email_xpath = (By.XPATH, '//input[@name="reg_email__"]')
    c_email_xpath = (By.XPATH, '//input[@name="reg_email_confirmation__"]')
    password_xpath = (By.XPATH, '//input[@name="reg_passwd__"]')
    day = (By.XPATH, '//select[@id="day"]')
    month = (By.XPATH, '//select[@id="month"]')
    year = (By.XPATH, '//select[@id="year"]')
    female = (By.XPATH, '//input[@id="u_0_6"]')
    male = (By.XPATH, '//input[@id="u_0_7"]')
    custom = (By.XPATH, '//input[@id="u_0_8"]')
    pronoun = (By.XPATH, '//select[@class="_7-16 _5dba"]')
    genderOptional_xpath = (By.XPATH, '//input[@id="u_0_13"]')

    #create one constructor to initialize the driver to indentify the elements

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, firstname):
        self.driver.find_element(self.first_name_xpath).send_keys(firstname)

    def setSurname(self, surname):
        self.driver.find_element(self.surname_xpath).send_keys(surname)

    def setEmail (self, email):
        self.driver.find_element(self.email_xpath).send_keys(email)

    def setSecondEmail(self, secondEmail):
        self.driver.find_element(self.c_email_xpath).send_keys(secondEmail)

    def setPassword(self, password):
        self.driver.find_element(self.password_xpath).send_keys(password)

    #Pick your birthday

    def birthdayDay(self,daySelect):
        Select(self.driver.find_element(self.day)).select_by_index(daySelect)

    def birthdayMonth(self, monthSelect):
        Select(self.driver.find_element(self.month)).select_by_index(monthSelect)

    def birthdayYear(self, yearSelect):
        Select(self.driver.find_element(self.year)).select_by_visible_text(yearSelect)

    def genderFemale(self):

        gender = self.driver.find_element(self.female)

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

        gender = self.driver.find_element(self.male)

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

        gender = self.driver.find_element(self.custom)

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
        Select(self.driver.find_element(self.pronoun)).select_by_value(pronounCheck)

    def optionalGenderInput(self, genderOptional):
        self.driver.find_element(self.genderOptional_xpath).send_keys(genderOptional)

