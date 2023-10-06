__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestAllPeople:

    def test_all_people(self, test_login):
        driver = test_login


        # All People Page Test
        driver.find_element(By.XPATH, Locator.people_dropdown).click()
        driver.find_element(By.XPATH, Locator.all_people).click()

        assert driver.find_element(By.XPATH, Locator.check_all_people).is_displayed()
