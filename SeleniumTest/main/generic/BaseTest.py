from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from main.utility import *
from main.utility import xmlReader as Env


class BaseTest:
    driver = ""
    logger = HTMlLogger()

    def __init__(self):
        pass

    def TestCaseInit(self, f1_logger):
        BaseTest.f1_logger = f1_logger
        BaseTest.EnvironmentValue = Env.XmlReader()
        BaseTest.driver = webdriver.Chrome(ChromeDriverManager().install())
        BaseTest.driver.maximize_window()
        BaseTest.driver.implicitly_wait(5)
        BaseTest.driver.get(self.EnvironmentValue.getValue("Url"))

    @classmethod
    def getDriver(cls):
        return cls.driver

    @staticmethod
    def TestCaseExit(log):
        BaseTest.driver.quit()
        log.close_report()
