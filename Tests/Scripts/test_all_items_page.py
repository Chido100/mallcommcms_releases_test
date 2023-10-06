__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestAllItems:

    def test_all_items(self, test_login):
        driver = test_login


        # All Items Test
        driver.find_element(By.XPATH, Locator.items_dropdown).click()
        driver.find_element(By.XPATH, Locator.all_items).click()

        assert driver.find_element(By.XPATH, Locator.check_page).is_displayed()
