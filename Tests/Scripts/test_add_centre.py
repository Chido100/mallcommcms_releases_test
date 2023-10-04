__author__ = 'Chidozie Amefule'

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestAddCentre(EnvironmentSetup):

    def test_add_centre(self):
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

        # Add centre
        driver.find_element(By.XPATH, Locator.manage_dropdown).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.add_centre).click()
        sleep(2)
        # Enter centre name
        enter_centre_name = driver.find_element(By.XPATH, Locator.centre_name)
        enter_centre_name.clear()
        enter_centre_name.send_keys(TestData.centre_name)
        # Select centre owner
        driver.find_element(By.XPATH, Locator.centre_owner_dropdown_button).click()
        sleep(2)
        driver.find_element(By.XPATH, Locator.centre_owner_dropdown).click()
        # Select phone code
        driver.find_element(By.XPATH, Locator.phone_code_dropdown_button).click()
        driver.find_element(By.XPATH, Locator.phone_code_dropdown).click()
        # Select language
        driver.find_element(By.XPATH, Locator.add_centre_language_dropdown_button).click()
        driver.find_element(By.XPATH, Locator.add_centre_language_dropdown).click()
        # Select app
        driver.find_element(By.XPATH, Locator.add_centre_app_button).click()
        driver.find_element(By.XPATH, Locator.add_centre_app).click()
        sleep(1)
        # Click the create centre button
        driver.find_element(By.XPATH, Locator.add_centre_create_button).click()
        sleep(3)
        # confirm centre is created
        assert "/centre/config/" in driver.current_url
        print("Successfully created a new centre!")