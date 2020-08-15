import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class GoogleTest(unittest.TestCase):

    @staticmethod
    def test_reopen_google_url_and_close():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com")
        driver.implicitly_wait(30000)
        print(driver.current_url)
        driver.quit()

    @staticmethod
    def test_open_google_url_and_close():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com")
        driver.implicitly_wait(30000)
        print(driver.current_url)
        driver.quit()


if __name__ == "__main__":
    unittest.main()
