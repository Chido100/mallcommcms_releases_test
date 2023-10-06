__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestAllStores:

    def test_all_stores(self, test_login):
        driver = test_login

        # Test All Stores Page
        driver.find_element(By.XPATH, Locator.stores_dropdown).click()
        driver.find_element(By.XPATH, Locator.all_stores).click()
        sleep(2)
        driver.find_element(By.XPATH, Locator.edit_store_button).click()
        driver.find_element(By.XPATH, Locator.update_store_button).click()

        assert driver.find_element(By.XPATH, Locator.check_all_stores).is_displayed()