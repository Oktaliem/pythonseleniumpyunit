import unittest

from main.generic.BaseTest import *
from main.pages import *
from main.utility import *


class Scenario3(unittest.TestCase, BaseTest):
    logger = HTMlLogger()  # function_logger(logging.INFO, logging.ERROR)

    @classmethod
    def setUp(cls):
        BaseTest().TestCaseInit(cls.logger)

    def test_scenario3(self):
        self.logger.assert_testcase_log("test_Scenario3")
        driver = BaseTest().getDriver()
        try:
            login_page = Login(driver, self.logger)
            login_page.login()

            my_account_page = MyAccount(driver, self.logger)
            my_account_page.navigate_to_order_history()
            my_account_page.get_historical_orders()

            login_page.logout()
        except Exception as e:
            self.logger.assert_step_fail_log(driver, str(e))

    @classmethod
    def tearDown(cls):
        BaseTest().TestCaseExit(cls.logger)


if __name__ == "__main__":
    unittest.main()
