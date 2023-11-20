__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import TestData


class TestManageCentreTags:

    def test_manage_centre_tags(self, test_login):
        driver = test_login

        driver.find_element(By.XPATH, Locator.manage_dropdown).click()

        # Navigate to the centre tags
        tags_management = driver.find_element(By.XPATH, Locator.tags_management)
        centre_tags = driver.find_element(By.XPATH, Locator.centre_tags)
        hover = ActionChains(driver).move_to_element(tags_management).move_to_element(centre_tags).click()
        hover.perform()

        # Add tag
        driver.find_element(By.XPATH, Locator.add_tag_button).click()

        driver.find_element(By.XPATH, Locator.tag).send_keys(TestData.tag)
        driver.find_element(By.XPATH, Locator.display_label).send_keys(TestData.display_label)

        driver.find_element(By.XPATH, )

        
