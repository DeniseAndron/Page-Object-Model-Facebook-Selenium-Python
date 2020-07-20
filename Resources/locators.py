from selenium.webdriver.common.by import By


class MainPageLocators(object):
    #Login page locators
    textbox_username_id = (By.ID,"email")
    textbox_password_id = (By.ID,"pass")
    button_login_id = (By.ID,"u_0_b")


    #Sign up page

    first_name_xpath = (By.XPATH, '//input[@name="firstname"]')
    surname_xpath = (By.XPATH, '//input[@name="lastname"]')
    email_xpath = (By.XPATH, '//input[@name="reg_email__"]')
    c_email_xpath = (By.XPATH, '//input[@name="reg_email_confirmation__"]')
    password_xpath = (By.XPATH, '//input[@name="reg_passwd__"]')
    day = (By.XPATH, '//select[@id="day"]')
    month = (By.XPATH, '//select[@id="month"]')
    year = (By.XPATH, '//select[@id="year"]')
    female = (By.XPATH, '//input[@id="u_0_6"]')
    male = (By.XPATH,'//input[@id="u_0_7"]')
    custom = (By.XPATH,'//input[@id="u_0_8"]')
    pronoun = (By.XPATH,'//select[@class="_7-16 _5dba"]')
    genderOptional_xpath = (By.XPATH, '//input[@id="u_0_13"]')

    #Content page
    login_error_message = (By.XPATH, '//div[@id="globalContainer"]/div[3]/div/div/div' )
    click_on_profile_page = (By.XPATH, '//div[@id="u_0_a"]/div[1]/div[1]/div')

