import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class GoogleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_reopen_google_url_and_close(self):
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(30000)
        print(self.driver.current_url)

    def test_open_google_url_and_close(self):
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(30000)
        print(self.driver.current_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
