import unittest

from Main.Generic.BaseTest import *
from Main.Pages import *
from Main.Utility import *


class Scenario3(unittest.TestCase, BaseTest):
    logger = HTMlLogger()  # function_logger(logging.INFO, logging.ERROR)

    @classmethod
    def setUp(cls):
        BaseTest().TestCaseInit(cls.logger)

    def test_Scenario3(self):
        self.logger.assert_testcase_log("test_Scenario3")
        driver = BaseTest().getDriver()
        try:
            pglogin = Login(driver, self.logger)
            pglogin.login()

            pgMyAccount = MyAccount(driver, self.logger)
            pgMyAccount.navigateToOrderHistory()
            pgMyAccount.getHistoricalOrders()

            pglogin.logout()
        except Exception as e:
            self.logger.assert_step_fail_log(driver, str(e))

    @classmethod
    def tearDown(cls):
        BaseTest().TestCaseExit(cls.logger)


if __name__ == "__main__":
    unittest.main()
