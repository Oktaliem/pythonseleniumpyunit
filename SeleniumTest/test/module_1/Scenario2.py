import unittest

from ddt import ddt, data

from main.generic.BaseTest import *
from main.pages import *
from main.utility import *


def get_data(file_name, test_case_id):
    return ReadLine(file_name, test_case_id)


@ddt
class Scenario2(unittest.TestCase, BaseTest):
    logger = HTMlLogger()  # function_logger(logging.INFO, logging.ERROR)

    @classmethod
    def setUp(cls):
        BaseTest().TestCaseInit(cls.logger)

    @data(get_data("TestData.xlsx", 'test_Scenario2'))
    def test_scenario2(self, current_row):
        self.logger.assert_testcase_log("test_Scenario2")
        driver = BaseTest().getDriver()
        try:
            login_page = Login(driver, self.logger)
            login_page.login()

            home_page = Home(driver, self.logger)
            home_page.navigate_to_casual_dress()

            casual_dress_page = CasualDress(driver, self.logger)
            casual_dress_page.select_size_medium()
            casual_dress_page.select_casual_dress()

            printed_dress_page = PrintedDress(driver, self.logger)
            printed_dress_page.select_quantity(current_row['Quntity'])
            printed_dress_page.add_item_to_cart()
            printed_dress_page.continue_shopping()

            home_page.navigate_to_t_shirts()

            t_shirt_page = TShirt(driver, self.logger)
            t_shirt_page.select_size_small()
            t_shirt_page.select_t_shirt()

            pg_faded_t_shirt = FadedTShirt(driver, self.logger)
            pg_faded_t_shirt.select_quantity(current_row['Quntity'])
            pg_faded_t_shirt.select_color(current_row['Color'])
            pg_faded_t_shirt.add_item_to_cart()
            pg_faded_t_shirt.perform_to_check_out()

            order_page = Order(driver, self.logger)
            order_page.proceed_to_checkout()
            order_page.proceed_to_checkout_in_address()
            order_page.proceed_to_checkout_in_shipping()
            order_page.verify_terms_of_service_error()
            order_page.accept_terms_of_service()
            order_page.proceed_to_checkout_in_shipping()
            order_page.select_payment_mode(current_row['Payment Mode'])
            order_page.confirm_order()

        except Exception as e:
            self.logger.assert_step_fail_log(driver, str(e))

    @classmethod
    def tearDown(cls):
        BaseTest().TestCaseExit(cls.logger)


if __name__ == "__main__":
    unittest.main()
