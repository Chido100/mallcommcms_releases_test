__author__ = 'Chidozie Amefule'



from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestAddItem:

    def test_add_item(self, test_login):
        driver = test_login


        # Add New Item
        driver.find_element(By.XPATH, Locator.items_dropdown).click()
        driver.find_element(By.XPATH, Locator.add_new_item).click()
