__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestAwards:

    def test_all_awards(self, test_login):
        driver = test_login


        # Test Awards Page
        driver.find_element(By.XPATH, Locator.people_dropdown).click()
        driver.find_element(By.XPATH, Locator.awards).click()

        assert driver.find_element(By.XPATH, Locator.check_awards).is_displayed()
