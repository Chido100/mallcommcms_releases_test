__author__ = 'Chidozie Amefule'

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestAddNewTicket(EnvironmentSetup):

    def test_add_new_ticket(self):
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

        # Add new ticket
        driver.find_element(By.XPATH, Locator.ticketing_dropdown).click()
        driver.find_element(By.XPATH, Locator.add_new_ticket).click()
        sleep(2)
        driver.find_element(By.XPATH, Locator.select_category_dropdown).click()
        driver.find_element(By.XPATH, Locator.selected_category).click()

        driver.find_element(By.XPATH, Locator.select_store_name_dropdown).click()
        driver.find_element(By.XPATH, Locator.selected_store).click()

        #driver.find_element(By.XPATH, Locator.select_a_person_dropdown).click()
        #driver.find_element(By.XPATH, Locator.selected_person).click()

        driver.find_element(By.XPATH, Locator.submit_add_ticket_button).click()

        title = driver.find_element(By.XPATH, Locator.ticket_title)
        title.send_keys(TestData.ticket_title)

        company = driver.find_element(By.XPATH, Locator.company)
        company.send_keys(TestData.company)

        name = driver.find_element(By.XPATH, Locator.ticket_creator_name_field)
        name.send_keys(TestData.ticket_creator_name)

        detail = driver.find_element(By.XPATH, Locator.ticket_details)
        detail.send_keys(TestData.ticket_details)

        driver.find_element(By.XPATH, Locator.ticket_end_date).click()
        driver.find_element(By.XPATH, Locator.selected_end_date).click()

        driver.find_element(By.XPATH, Locator.date_apply).click()

        place = driver.find_element(By.XPATH, Locator.place_of_work)
        place.send_keys(TestData.place_of_work)

        driver.find_element(By.XPATH, Locator.ticket_add_button).click()