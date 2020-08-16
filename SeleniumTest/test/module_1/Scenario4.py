import unittest

from ddt import ddt, data

from main.generic.BaseTest import *
from main.pages import *
from main.utility import *


def getData(fileName,TestCaseID):
    return ReadLine(fileName,TestCaseID)

@ddt
class Scenario4(unittest.TestCase, BaseTest):
    logger = HTMlLogger()  # function_logger(logging.INFO, logging.ERROR)

    @classmethod
    def setUp(cls):
        BaseTest().TestCaseInit(cls.logger)

    @data(getData("TestData.xlsx", 'test_Scenario4'))
    def test_Scenario4(self, currentRow):
        self.logger.assert_testcase_log("test_Scenario4")
        driver = BaseTest().getDriver()
        try:
            homePage = Home(driver, self.logger)
            homePage.navigateToTShirts()

            tShirtPage = TShirt(driver, self.logger)
            tShirtPage.selectSizeSmall()
            tShirtPage.selectTShirt()

            fadedTShirtPage = FadedTShirt(driver, self.logger)
            fadedTShirtPage.selectQuantity(currentRow['Quntity'])
            fadedTShirtPage.selectColor(currentRow['Color'])
            fadedTShirtPage.addItemToCart()
            fadedTShirtPage.proceedToCheckOut()

            orderPage = Order(driver, self.logger)
            orderPage.ProceedToCheckout()

            loginPage = Login(driver, self.logger)
            loginPage.signIn()

            orderPage.ProceedToCheckoutInAddress()
            orderPage.ProceedToCheckoutInShipping()
            orderPage.verifyTermsOfServiceError()
            orderPage.acceptTermsOfService()
            orderPage.ProceedToCheckoutInShipping()
            orderPage.selectPaymentMode(currentRow['Payment Mode'])
            orderPage.confirmOrder()

        except Exception as e:
            self.logger.assert_step_fail_log(driver, str(e))

    @classmethod
    def tearDown(cls):
        BaseTest().TestCaseExit(cls.logger)


if __name__ == "__main__":
    unittest.main()