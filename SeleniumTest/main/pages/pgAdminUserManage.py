import time

from selenium.webdriver.common.by import By
from main.generic import *


class AdminUserManage(BasePage):

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        BasePage.__init__(self, driver, logger)

    locator_dictionary = {
        "edtUserName": (By.ID, 'searchSystemUser_userName'),
        "lstUserRole": (By.XPATH, "//select[@id='searchSystemUser_userType']"),
        "edtEmployeeName": (By.ID, "searchSystemUser_employeeName_empName"),
        "lstStatus": (By.XPATH, "//select[@id='searchSystemUser_status']"),
        "btnSearch": (By.NAME, "_search"),
        "lnkSearchResult": (By.NAME, "//table[@id='resultTable']//tr/td/a")
    }

    def search_system_user(self, current_row):
        self.edtUserName.send_keys(current_row.get("SystemUser"))
        self.logger.info("Enter System user name as " + current_row.get("SystemUser"))

        super().selectElementByText(self.lstUserRole, current_row.get("UserRole"))
        self.logger.info("Enter System user role as " + current_row.get("UserRole"))

        self.edtEmployeeName.send_keys(current_row.get("EmployeeName"))
        self.logger.info("Enter employee user name as " + current_row.get("EmployeeName"))

        super().selectElementByText(self.lstStatus, current_row.get("EmpStatus"))
        self.logger.info("Select Status as " + current_row.get("EmpStatus"))

        self.btnSearch.click()
        self.logger.info("Successfully Click on Search button")

        super().waitAndAbort(self.lnkSearchResult)
        time.sleep(5)
