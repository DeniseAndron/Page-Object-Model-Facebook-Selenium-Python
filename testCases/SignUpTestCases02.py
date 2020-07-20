
import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys

sys.path.append("C://Users/Denisa/Desktop/selenium/facebook")
from pageObjects.SignUpPage import SignUpPage
from Resources.TestData import TestData
from testCases.BaseTest import facebookTestBase





class SignUpTest(facebookTestBase):

    @classmethod
    def setUpClass(cls):
        # to call the setUp() method of base class or super class.
        super().setUpClass()

    def test_001_SignUpFirstName(self):
        sp = SignUpPage(self.driver)
        sp.setFirstName(TestData.firstname)

    def test_002_SignUpSurname(self):
        sp = SignUpPage(self.driver)
        sp.setSurname(TestData.surname)

    def test_003_Email(self):
        sp = SignUpPage(self.driver)
        sp.setEmail(TestData.email)
        time.sleep(2)

    def test_004_secondEmail(self):
        sp = SignUpPage(self.driver)
        sp.setSecondEmail(TestData.secondEmail)

    def test_005_SignInPassword(self):
        sp = SignUpPage(self.driver)
        sp.setPassword(TestData.password)
        time.sleep(2)

    def test_006_PickDay(self):
        sp = SignUpPage(self.driver)
        sp.birthdayDay(TestData.daySelect)

    def test_007_PickMonth(self):
        sp = SignUpPage(self.driver)
        sp.birthdayMonth(TestData.monthSelect)

    def test_008_PickYear(self):
        sp = SignUpPage(self.driver)
        sp.birthdayYear(TestData.yearSelect)


    def test_009_FemalePick(self):
        sp = SignUpPage(self.driver)
        sp.genderFemale()

    def test_01_MalePick(self):
        sp = SignUpPage(self.driver)
        sp.genderMale()

    def test_02_CustomPick(self):
        sp = SignUpPage(self.driver)
        sp.genderCustom()
        time.sleep(3)

    def test_03_PronounPick(self):
        sp = SignUpPage(self.driver)
        sp.pronounSelect(TestData.pronounCheck)

    def test_04_optionalGenderPick(self):
        sp = SignUpPage(self.driver)
        sp.optionalGenderInput(TestData.genderOptional)


if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner (output="C:\\Users\\Denisa\\Desktop\\selenium\\facebook\\reports"))