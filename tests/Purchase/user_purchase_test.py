from pages.purchase.user_purchase import UserPurchasePage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class UserPurchaseTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.userPur = UserPurchasePage(self.driver)
        self.ts = TestStatus(self.driver)


    def test_userPurchaseSuccess(self):
        self.userPur.userPurchase("Blue Faded Shirt Sleeve T-shirt",
                                  "testuser006@gmail.com","12345")






