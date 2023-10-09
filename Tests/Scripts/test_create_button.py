__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import TestData


class TestCreateNewButton:

    def test_create_new_button(self, test_login):
        driver = test_login

        # Test Create a New Button
        driver.find_element(By.XPATH, Locator.manage_dropdown).click()
        sleep(2)

        # Hover and click on element
        your_centre = driver.find_element(By.XPATH, Locator.your_centre_dropdown)
        manage_buttons = driver.find_element(By.XPATH, Locator.manage_your_buttons)
        hover = ActionChains(driver).move_to_element(your_centre).move_to_element(manage_buttons).click()
        hover.perform()

        driver.find_element(By.XPATH, Locator.add_new_button).click()
        
        button_name = driver.find_element(By.XPATH, Locator.button_name)
        button_name.send_keys(TestData.button_name)

        driver.find_element(By.XPATH, Locator.create_button_button).click()

        assert "/manage/edit-button/" in driver.current_url






    