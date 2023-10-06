__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestAddNewTemplate:

    def test_add_new_template(self, test_login):
        driver = test_login


        # Add new template
        driver.find_element(By.XPATH, Locator.manage_dropdown).click()
        driver.find_element(By.XPATH, Locator.templates).click()

        driver.find_element(By.XPATH, Locator.add_new_template_button).click()
        driver.find_element(By.XPATH, Locator.template_name).send_keys(TestData.template_name)

        driver.find_element(By.XPATH, Locator.template_display_name).send_keys(TestData.template_display_name)

        driver.find_element(By.XPATH, Locator.template_data).send_keys(TestData.template_data)

        driver.find_element(By.XPATH, Locator.template_save_button).click()
        sleep(2)

        assert "/templates/manage/edit/" in driver.current_url

