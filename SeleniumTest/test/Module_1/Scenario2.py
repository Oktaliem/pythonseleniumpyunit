import unittest

from ddt import ddt, data

from Main.Generic.BaseTest import *
from Main.Pages import *
from Main.Utility import *


def getData(fileName,TestCaseID):
    return ReadLine(fileName,TestCaseID)

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
            pglogin = Login(driver, self.logger)
            pglogin.login()

            pgHome = Home(driver,self.logger)
            pgHome.navigateToCasualDress()

            pgCasualDress = CasualDress(driver,self.logger)
            pgCasualDress.selectSizeMedium()
            pgCasualDress.selectCasualDress()

            pgPrintedDress = PrintedDress(driver,self.logger)
            pgPrintedDress.selectQuantity(currentRow['Quntity'])
            pgPrintedDress.addItemToCart()
            pgPrintedDress.ContinueShopping()

            pgHome.navigateToTshirts()

            pgTShirt = TShirt(driver,self.logger)
            pgTShirt.selectSizesmall()
            pgTShirt.selectTShirt()

            pgFadedTshirt = FadedTShirt(driver,self.logger)
            pgFadedTshirt.selectQuantity(currentRow['Quntity'])
            pgFadedTshirt.selectColor(currentRow['Color'])
            pgFadedTshirt.addItemToCart()
            pgFadedTshirt.proceedToCheckOut()

            pgOrder = Order(driver, self.logger)
            pgOrder.ProceedToCheckout()
            # pgOrder.selectDeliveryAddrAsBillingAddr()
            pgOrder.ProceedToCheckoutInAddress()
            pgOrder.ProceedToCheckoutInShipping()
            pgOrder.verifyTermsOfServiceError()
            pgOrder.acceptTermsOfService()
            pgOrder.ProceedToCheckoutInShipping()
            pgOrder.selectPaymentMode(currentRow['Payment Mode'])
            pgOrder.confirmOrder()

        except Exception as e:
            self.logger.assert_step_fail_log(driver, str(e))

    @classmethod
    def tearDown(cls):
        BaseTest().TestCaseExit(cls.logger)


if __name__ == "__main__":
    unittest.main()
