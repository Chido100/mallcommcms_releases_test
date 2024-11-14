__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import TestData


class TestManageYourCentre:

    def test_manage_your_centre(self, test_login):
        driver = test_login


        # Navigate to Manage your centre page  
        driver.find_element(By.XPATH, Locator.manage_dropdown).click()

        # Hover and click on Manage your centre button
        your_centre = driver.find_element(By.XPATH, Locator.your_centre_dropdown)
        manage_your_centre = driver.find_element(By.XPATH, Locator.manage_your_centre)
        hover = ActionChains(driver).move_to_element(your_centre).move_to_element(manage_your_centre).click()
        hover.perform()

        driver.find_element(By.XPATH, Locator.manage_your_centre_update_button).click()

        alert = driver.find_element(By.XPATH, Locator.manage_your_centre_update_success)

        assert alert.is_displayed()
