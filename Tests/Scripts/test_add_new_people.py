__author__ = 'Chidozie Amefule'

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestAddPeople(EnvironmentSetup):

    def test_add_people(self):
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

        # Add New People
        driver.find_element(By.XPATH, Locator.people_dropdown).click()
        driver.find_element(By.XPATH, Locator.add_new_people).click()
        first_name = driver.find_element(By.XPATH, Locator.first_name)
        first_name.clear()
        first_name.send_keys(TestData.last_name)
        last_name = driver.find_element(By.XPATH, Locator.last_name)
        last_name.clear()
        last_name.send_keys(TestData.last_name)
        people_email = driver.find_element(By.XPATH, Locator.add_people_email)
        people_email.clear()
        people_email.send_keys(TestData.people_email)
        password = driver.find_element(By.XPATH, Locator.password)
        password.send_keys(TestData.people_password)
        confirm_password = driver.find_element(By.XPATH, Locator.confirm_password)
        confirm_password.send_keys(TestData.people_confirm_password)

        driver.find_element(By.XPATH, Locator.select_store_dropdown).click()
        driver.find_element(By.XPATH, Locator.add_people_store_selected).click()
        driver.find_element(By.XPATH, Locator.select_role_dropdown).click()
        driver.find_element(By.XPATH, Locator.selected_role).click()

        driver.find_element(By.XPATH, Locator.create_button).click()