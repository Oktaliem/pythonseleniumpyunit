import unittest

from ddt import ddt, data

from Main.Generic.BaseTest import *
from Main.Pages import *
from Main.Utility import *


def getData(fileName, TestCaseID):
    return ReadLine(fileName, TestCaseID)


@ddt
class Scenario2(unittest.TestCase, BaseTest):
    logger = HTMlLogger()  # function_logger(logging.INFO, logging.ERROR)

    @classmethod
    def setUp(cls):
        BaseTest().TestCaseInit(cls.logger)

    @data(getData("TestData.xlsx", 'test_Scenario2'))
    def test_Scenario2(self, currentRow):
        self.logger.assert_testcase_log("test_Scenario2")
        driver = BaseTest().getDriver()
        try:
            loginPage = Login(driver, self.logger)
            loginPage.login()

            homePage = Home(driver, self.logger)
            homePage.navigateToCasualDress()

            casualDressPage = CasualDress(driver, self.logger)
            casualDressPage.selectSizeMedium()
            casualDressPage.selectCasualDress()

            printedDressPage = PrintedDress(driver, self.logger)
            printedDressPage.selectQuantity(currentRow['Quntity'])
            printedDressPage.addItemToCart()
            printedDressPage.ContinueShopping()

            homePage.navigateToTShirts()

            tShirtPage = TShirt(driver, self.logger)
            tShirtPage.selectSizeSmall()
            tShirtPage.selectTShirt()

            pgFadedTShirt = FadedTShirt(driver, self.logger)
            pgFadedTShirt.selectQuantity(currentRow['Quntity'])
            pgFadedTShirt.selectColor(currentRow['Color'])
            pgFadedTShirt.addItemToCart()
            pgFadedTShirt.proceedToCheckOut()

            orderPage = Order(driver, self.logger)
            orderPage.ProceedToCheckout()
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
