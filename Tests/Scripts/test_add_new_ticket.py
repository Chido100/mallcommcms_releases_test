__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestAddNewTicket:

    def test_add_new_ticket(self, test_login):
        driver = test_login


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