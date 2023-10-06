__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestAddStore:

    def test_add_store(self, test_login):
        driver = test_login


        # Add store
        driver.find_element(By.XPATH, Locator.stores_dropdown).click()
        driver.find_element(By.XPATH, Locator.add_new_store).click()
        driver.find_element(By.XPATH, Locator.select_store_name_dropdown).click()
        driver.find_element(By.XPATH, Locator.store_selected).click()

        driver.find_element(By.XPATH, Locator.create_store_button).click()

        assert driver.find_element(By.XPATH, Locator.success).is_displayed()
