import unittest

from ddt import ddt, data

from main.generic.BaseTest import *
from main.pages import *
from main.utility import *


def getData(fileName, TestCaseID):
    return ReadLine(fileName, TestCaseID)


@ddt
class Scenario1(unittest.TestCase, BaseTest):
    logger = HTMlLogger()  # function_logger(logging.INFO, logging.ERROR)

    @classmethod
    def setUp(cls):
        BaseTest().TestCaseInit(cls.logger)

    @data(getData("TestData.xlsx", 'test_Scenario1'))
    def test_Scenario1(self, currentRow):
        self.logger.assert_testcase_log("test_Scenario1")
        driver = BaseTest().getDriver()
        try:
            homePage = Home(driver, self.logger)
            homePage.navigateToCasualDress()

            casualDressPage = CasualDress(driver, self.logger)
            casualDressPage.sortBy()
            casualDressPage.selectSizeMedium()
            time.sleep(2)

            casualDressPage.selectCasualDress()

            printedDressPage = PrintedDress(driver, self.logger)
            printedDressPage.selectQuantity(currentRow['Quntity'])
            printedDressPage.addItemToCart()
            printedDressPage.proceedToCheckOut()

            orderPage = Order(driver, self.logger)
            orderPage.deleteSingleItemFromCart()
            orderPage.verifyEmptyCart()
        except Exception as e:
            self.logger.assert_step_fail_log(driver, str(e))

    @classmethod
    def tearDown(cls):
        BaseTest().TestCaseExit(cls.logger)
        # cls.logger.close_report()


if __name__ == "__main__":
    unittest.main()
