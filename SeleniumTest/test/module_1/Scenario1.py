import unittest

from ddt import ddt, data

from main.generic.BaseTest import *
from main.pages import *
from main.utility import *


def get_data(file_name, test_case_id):
    return ReadLine(file_name, test_case_id)


@ddt
class Scenario1(unittest.TestCase, BaseTest):
    logger = HTMlLogger()  # function_logger(logging.INFO, logging.ERROR)

    @classmethod
    def setUp(cls):
        BaseTest().TestCaseInit(cls.logger)

    @data(get_data("TestData.xlsx", 'test_Scenario1'))
    def test_scenario1(self, current_row):
        self.logger.assert_testcase_log("test_Scenario1")
        driver = BaseTest().getDriver()
        try:
            home_page = Home(driver, self.logger)
            home_page.navigate_to_casual_dress()

            casual_dress_page = CasualDress(driver, self.logger)
            casual_dress_page.sort_by()
            casual_dress_page.select_size_medium()
            time.sleep(2)

            casual_dress_page.select_casual_dress()

            printed_dress_page = PrintedDress(driver, self.logger)
            printed_dress_page.select_quantity(current_row['Quntity'])
            printed_dress_page.add_item_to_cart()
            printed_dress_page.proceed_to_check_out()

            order_page = Order(driver, self.logger)
            order_page.delete_single_item_from_cart()
            order_page.verify_empty_cart()
        except Exception as e:
            self.logger.assert_step_fail_log(driver, str(e))

    @classmethod
    def tearDown(cls):
        BaseTest().TestCaseExit(cls.logger)
        # cls.logger.close_report()


if __name__ == "__main__":
    unittest.main()
