__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import TestData


class TestManageAccessLevel:

    def test_manage_access_level(self, test_login):
        driver = test_login


        driver.find_element(By.XPATH, Locator.manage_dropdown).click()
        sleep(2)

        # Navigate to the Manage access levels page
        your_centre = driver.find_element(By.XPATH, Locator.your_centre_dropdown)
        manage_access_level = driver.find_element(By.XPATH, Locator.manage_access_level)
        hover = ActionChains(driver).move_to_element(your_centre).move_to_element(manage_access_level).click()
        hover.perform()

        # Create access level
        access_level = driver.find_element(By.XPATH, Locator.new_access_level)
        access_level.send_keys(TestData.access_level_name)

        driver.find_element(By.XPATH, Locator.access_level_create_button).click()

        alert = driver.find_element(By.XPATH, Locator.access_level_success_alert)
        # Check that access level is created successfully
        assert alert.is_displayed()
