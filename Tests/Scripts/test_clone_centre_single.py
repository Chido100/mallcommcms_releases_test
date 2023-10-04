__author__ = 'Chidozie Amefule'

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData
from imagefiles import profile_image


class TestSingleCentreClone(EnvironmentSetup):

    def test_single_centre_clone(self):
        driver = self.driver

        # login procedure
        enter_email = driver.find_element(By.XPATH, Locator.login_email)
        enter_email.clear()
        enter_email.send_keys(TestData.valid_email)
        driver.find_element(By.XPATH, Locator.login_next_button).click()
        sleep(1)

        driver.find_element(By.XPATH, Locator.login_with_toolbox).click()

        print_email = driver.find_element(By.XPATH, Locator.print_email)
        print_email.send_keys(TestData.valid_email)
        driver.find_element(By.XPATH, Locator.print_email_next_button).click()

        print_password = driver.find_element(By.XPATH, Locator.print_password)
        print_password.send_keys(TestData.password)
        sleep(2)

        driver.find_element(By.XPATH, Locator.print_password_next_button).click()
        sleep(2)

        driver.find_element(By.XPATH, Locator.select_database).click()
        sleep(2)

        # Create single clone centre
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

        driver.find_element(By.XPATH, Locator.create_clone_button).click()
        driver.find_element(By.XPATH, Locator.agreement_modal).click()

        assert driver.find_element(By.XPATH, Locator.clone_complete).is_displayed()