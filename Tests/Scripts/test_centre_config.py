__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestCentreConfig:

    def test_centre_config(self, test_login):
        driver = test_login


        # Test Centre Config
        driver.find_element(By.XPATH, Locator.manage_dropdown).click()
        driver.find_element(By.XPATH, Locator.system_config_dropdown).click()
