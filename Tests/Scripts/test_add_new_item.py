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
        driver.find_element(By.XPATH, Locator.item_title).send_keys(TestData.item_title)
        driver.find_element(By.XPATH, Locator.save_continue_button).click()

        driver.find_element(By.XPATH, Locator.add_content_save_and_next_button).click()

        # Find the toggle element to select
        toggle_element = driver.find_element(By.XPATH, Locator.assign_button_toggle)

        # Check if the toggle is not already selected
        if not toggle_element.is_selected():
            toggle_element.click()

        driver.find_element(By.XPATH, Locator.assign_button_save_and_next_button).click()

        driver.find_element(By.XPATH, Locator.response_buttons_save_and_next_button).click()

        driver.find_element(By.XPATH, Locator.add_new_item_publish).click()

        # Check that user is navigated to the all items page
        assert "/items/all-items/" in driver.current_url
        

