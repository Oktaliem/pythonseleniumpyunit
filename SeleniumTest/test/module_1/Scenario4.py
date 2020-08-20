import unittest

from ddt import ddt, data

from main.generic.BaseTest import *
from main.pages import *
from main.utility import *


def get_data(file_name, test_case_id):
    return ReadLine(file_name, test_case_id)


@ddt
class Scenario4(unittest.TestCase, BaseTest):
    logger = HTMlLogger()  # function_logger(logging.INFO, logging.ERROR)

    @classmethod
    def setUp(cls):
        BaseTest().TestCaseInit(cls.logger)

    @data(get_data("TestData.xlsx", 'test_Scenario4'))
    def test_scenario4(self, current_row):
        self.logger.assert_testcase_log("test_Scenario4")
        driver = BaseTest().getDriver()
        try:
            home_page = Home(driver, self.logger)
            home_page.navigate_to_t_shirts()

            t_shirt_page = TShirt(driver, self.logger)
            t_shirt_page.select_size_small()
            t_shirt_page.select_t_shirt()

            faded_t_shirt_page = FadedTShirt(driver, self.logger)
            faded_t_shirt_page.select_quantity(current_row['Quntity'])
            faded_t_shirt_page.select_color(current_row['Color'])
            faded_t_shirt_page.add_item_to_cart()
            faded_t_shirt_page.perform_to_check_out()

            order_page = Order(driver, self.logger)
            order_page.proceed_to_checkout()

            login_page = Login(driver, self.logger)
            login_page.sign_in()

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
