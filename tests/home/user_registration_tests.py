from pages.home.user_registration_page import UserRegistrationPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp")
class UserRegistrationTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.userReg = UserRegistrationPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_userRegistrationSuccess(self):
        self.userReg.userRegistration('007007@gmail.com','Automation','Practice','xyz@123','ABC PLC',
            'Outer Ring Road','Prime square','Florida','00002','HTC','9890000000','9881012345')
        result2 = self.userReg.verifyUserRegistrationSucess()
        self.ts.markFinal("test_userRegistrationSuccess",result2,
                          "User registration was sucessful")


    @pytest.mark.run(order=1)
    def test_userRegistrationFails(self):
        self.userReg.userRegistration('556733@gmail.com', 'Sony', 'TV', 'xyz@123', 'ABC PLC',
                                 'Outer Ring Road', 'Prime square', 'Florida', '', 'HTC', '9890000000',
                                 '9881012345')
        result = self.userReg.verifyUserRegistrationFails()
        self.ts.markFinal("test_userRegistrationFails",result,"User registration failed")











# ff = UserRegistrationTests()
# ff.test_userRegistration()

