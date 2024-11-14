"""

__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData
from imagefiles import profile_image


class TestMultipleCentreClone:

    def test_multiple_centre_clone(self, test_login):
        driver = test_login


        # Test Clone Multiple Centre
        driver.find_element(By.XPATH, Locator.manage_dropdown).click()
        driver.find_element(By.XPATH, Locator.clone_centre).click()

        driver.find_element(By.XPATH, Locator.select_a_centre).click()
        driver.find_element(By.XPATH, Locator.selected_centre_to_clone).click()
        sleep(2)
        # Upload image
        upload_image = driver.find_element(By.XPATH, Locator.choose_file_button).click()
        sleep(2)
        upload_image.send_keys(profile_image)
        sleep(2)

        clone_centre_name = driver.find_element(By.XPATH, Locator.clone_centre)
        clone_centre_name.send_keys(TestData.cloned_centre_name)

        driver.find_element(By.XPATH, Locator.clone_centre_plus_sign).click()
        sleep(2)
        
        clone_centre_name2 = driver.find_element(By.XPATH, Locator.clone_centre)
        clone_centre_name2.send_keys(TestData.cloned_centre_name_2)

        driver.find_element(By.XPATH, Locator.create_clone_button).click()
        driver.find_element(By.XPATH, Locator.agreement_modal).click()

        assert driver.find_element(By.XPATH, Locator.clone_complete).is_displayed()

        
"""

