from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class UserRegistrationPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _sign_in = 'login'
    _email_address= 'email_create'
    _create_account = 'SubmitCreate'
    _title = 'id_gender1'
    _first_name = 'customer_firstname'
    _last_name = 'customer_lastname'
    _email1 = 'email'
    _password = 'passwd'
    _dob_days = 'days'
    _dob_month = 'months'
    _dob_year = 'years'
    _company = 'company'
    _address_1 = 'address1'
    _address_2 = 'address2'
    _city = 'city'
    _state = 'id_state'
    _z = 'postcode'
    _country = 'id_country'
    _add_info = 'other'
    _home_phone = 'phone'
    _mobile_phone = 'phone_mobile'
    _register = 'submitAccount'


    def getDobDays(self):
        return self.driver.find_element(By.ID, self._dob_days)

    def getDobMonth(self):
        return self.driver.find_element(By.ID, self._dob_month)

    def getDobYear(self):
        return self.driver.find_element(By.ID, self._dob_year)


    def getState(self):
        return self.driver.find_element(By.ID, self._state)


    def clickSignInLink(self):
        self.elementClick(self._sign_in,locatorType='classname')


    def enterEmail(self,email):
        self.sendKeys(email,self._email_address)


    def clickCreateAccount(self):
        self.elementClick(self._create_account)


    def clickTitle(self):
        self.elementClick(self._title)


    def enterFirstName(self,fName):
        self.sendKeys(fName,self._first_name)


    def enterLastName(self,lName):
        self.sendKeys(lName,self._last_name)


    def clickEmail1(self):
        self.elementClick(self._email1)


    def enterPassword(self,pas):
        self.sendKeys(pas,self._password)


    def selcDobDays(self):
        self.days = Select(self.getDobDays())
        self.days.select_by_value('4')


    def selcDobMonth(self):
        self.month = Select(self.getDobMonth())
        self.month.select_by_value('5')

    def selcDobYear(self):
        self.year = Select(self.getDobYear())
        self.year.select_by_index(37)

    def enterCompany(self,com):
        self.sendKeys(com,self._company)


    def enterAddress1(self,ad1):
        self.sendKeys(ad1,self._address_1)


    def enterAddress2(self,ad2):
        self.sendKeys(ad2,self._address_2)


    def enterCity(self,cit):
        self.sendKeys(cit,self._city)


    def selcState(self):
        self.state = Select(self.getState())
        self.state.select_by_visible_text('Florida')

    def enterZipPin(self,zi):
        self.sendKeys(zi,self._z)



    def enterAddInfo(self,adi):
        self.sendKeys(adi,self._add_info)


    def enterHomePhone(self,hph):
        self.sendKeys(hph,self._home_phone)


    def enterMobilePhone(self,mph):
        self.sendKeys(mph,self._mobile_phone)


    def clickRegisterButton(self):
        self.elementClick(self._register)




    def userRegistration(self,email='',fName='',lName='',pas='',com='',ad1='',ad2='',
            cit='',zi='',adi='',hph='',mph=''):
        self.clickSignInLink()
        self.enterEmail(email)
        self.clickCreateAccount()
        self.clickTitle()
        self.enterFirstName(fName)
        self.enterLastName(lName)
        self.clickEmail1()
        self.enterPassword(pas)
        self.selcDobDays()
        self.selcDobMonth()
        self.selcDobYear()
        self.enterCompany(com)
        self.enterAddress1(ad1)
        self.enterAddress2(ad2)
        self.enterCity(cit)
        self.selcState()
        self.enterZipPin(zi)
        self.enterAddInfo(adi)
        self.enterHomePhone(hph)
        self.enterMobilePhone(mph)
        self.clickRegisterButton()

    def verifyUserRegistrationSucess(self):
        result = self.isElementPresent("//a[@class='logout']",
                                       locatorType="xpath")
        return result

    def verifyUserRegistrationFails(self):
        result = self.isElementPresent('//li[contains(text(),"The Zip/Postal code you\'ve entered is invalid")]'
                                       ,locatorType='xpath')

        return result















