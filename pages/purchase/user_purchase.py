from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time

class UserPurchasePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)



    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    _search_textbox = 'search_query_top'
    _search_button = "//form[@id='searchbox']//button[@type='submit']"
    _color= 'color_2'
    _size_dropdown = "group_1"
    _add_to_cart = "//span[contains(text(),'Add to cart')]"
    _ptc  = "//a[@class='btn btn-default button button-medium']//span"
    _ptc1 = "//a[@href='http://automationpractice.com/index.php?controller=order&step=1']//span"
    _email_field = "email"
    _password_field = "passwd"
    _sign_in = "SubmitLogin"
    _ptc2 = "//p[@class='cart_navigation clearfix']//button[@type='submit']//span"
    _terms = 'cgv'
    _ptc3 = "//p[@class='cart_navigation clearfix']//button[@type='submit']//span"
    _payment = 'bankwire'
    _confirm_order = "//button[@class='button btn btn-default button-medium']"

    def getSize(self):
        return self.driver.find_element(By.ID, self._size_dropdown)

    def enterSearchText(self,searchText):
        self.sendKeys(searchText, self._search_textbox)

    def clickSearchButton(self):
        self.elementClick(self._search_button,'xpath')

    def clickColor(self):
        self.elementClick(self._color)

    def selectSize(self):
        self.size = Select(self.getSize())
        self.size.select_by_value('2')

    def clickAddToCart(self):
        self.elementClick(self._add_to_cart,'xpath')


    def clickProceedToCheckout(self):
        self.elementClick(self._ptc,'xpath')

    def clickProceedToCheckout1(self):
        self.elementClick(self._ptc1,'xpath')

    def enterEmail(self,email):
        self.sendKeys(email,self._email_field)

    def enterPassword(self,password):
        self.sendKeys(password,self._password_field)

    def clickSignIn(self):
        self.elementClick(self._sign_in)

    def clickProceedToCheckout2(self):
        self.elementClick(self._ptc2,'xpath')

    def clickTerms(self):
        self.elementClick(self._terms)

    def clickclickProceedToCheckout3(self):
        self.elementClick(self._ptc3,'xpath')

    def clickPayByBankWire(self):
        self.elementClick(self._payment,'classname')

    def clickConfirmOrder(self):
        self.elementClick(self._confirm_order,'xpath')

    def userPurchase(self, searchText='', email='', password=''):
        sd = SeleniumDriver(self.driver)
        self.enterSearchText('Blue Faded Shirt Sleeve T-shirt')
        self.clickSearchButton()
        self.clickColor()
        self.selectSize()
        self.clickAddToCart()
        sd.waitForElement("//a[@class='btn btn-default button button-medium']//span", "xpath", 5, 0.5)
        self.clickProceedToCheckout()
        self.clickProceedToCheckout1()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickSignIn()
        self.clickProceedToCheckout2()
        self.clickTerms()
        self.clickclickProceedToCheckout3()
        self.clickPayByBankWire()
        self.clickConfirmOrder()







