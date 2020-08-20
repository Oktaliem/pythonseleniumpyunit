from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
import time


class MyAccount(PageFactory):

    def __init__(self, driver, logger):
        super().__init__()
        self.driver = driver
        self.logger = logger

    locators = {
        "btnCart": ('XPATH', "//*[@title='View my shopping cart']"),
        "btnOrderHistory": ('XPATH', "//a[@title='Orders']"),
        "tblOrderHistory": ("XPATH", "//*[@id='order-list']/tbody")
    }

    def navigate_to_cart(self):
        self.btnCart.click_button()
        self.logger.assert_step_log("PASS", 'Successfully navigated to Cart...')

    def navigate_to_order_history(self):
        self.btnOrderHistory.click_button()
        self.logger.assert_step_log("PASS", 'Successfully navigated to Order History...')

    def get_historical_orders(self):
        rows = self.tblOrderHistory.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        for row in rows:
            col = row.find_elements(By.TAG_NAME, "td")  # note: index start from 0, 1 is col 2
            col[5].click()
            self.logger.assert_step_log("PASS", 'Successfully verified Order History of ' + col[0].text)
            time.sleep(2)
            break
