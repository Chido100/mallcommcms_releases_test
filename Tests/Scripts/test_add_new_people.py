__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData



class TestAddPeople:

    def test_add_people(self, test_login):
        driver = test_login


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
        assert "/people/edit-person/" in driver.current_url
        print("Successfully added new people.")