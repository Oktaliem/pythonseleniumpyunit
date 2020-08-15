from com.oktaliem.test import BaseTest
from HtmlTestRunner import HTMLTestRunner

import unittest
import os


class GoogleTest(BaseTest.BaseTest):

    def test_reopen_google_url_and_close(self):
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(30000)
        print(self.driver.current_url)

    def test_open_google_url_and_close(self):
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(30000)
        print(self.driver.current_url)


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output=os.getcwd() + '/reports'))
