__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestCRMPage:

    def test_crm_page(self, test_login):
        driver = test_login


        driver.find_element(By.XPATH, Locator.people_dropdown).click()
        # Open CRM page
        driver.find_element(By.XPATH, Locator.crm).click()

        # Add new contact
        driver.find_element(By.XPATH, Locator.add_new_contact).click()
        # Enter CRM name
        crm_name = driver.find_element(By.XPATH, Locator.crm_contact_name)
        crm_name.send_keys(TestData.crm_name)
        # Select CRM store
        driver.find_element(By.XPATH, Locator.crm_store).click()
        driver.find_element(By.XPATH, Locator.crm_selected_store).click()
        # Type of contact
        driver.find_element(By.XPATH, Locator.crm_type_of_contact).click()
        driver.find_element(By.XPATH, Locator.crm_selected_type_contact).click()

        driver.find_element(By.XPATH, Locator.crm_add_contact_button).click()
        sleep(3)

        crm_page = driver.find_element(By.XPATH, Locator.crm_page)
        assert crm_page.is_displayed()





    

        
