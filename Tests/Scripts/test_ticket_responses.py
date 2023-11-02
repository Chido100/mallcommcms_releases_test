__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestTicketResponses:

    def test_ticket_responses(self, test_login):
        driver = test_login


        # Test Ticket Responses
        driver.find_element(By.XPATH, Locator.manage_dropdown).click()
        driver.find_element(By.XPATH, Locator.ticket_responses).click()
        driver.find_element(By.XPATH, Locator.add_response_button).click()

        driver.find_element(By.XPATH, Locator.response_button_dropdown).click()
        driver.find_element(By.XPATH, Locator.selected_response_button).click()

        driver.find_element(By.XPATH, Locator.response_order).send_keys(TestData.response_order)
        driver.find_element(By.XPATH, Locator.response_title).send_keys(TestData.response_title)
        driver.find_element(By.XPATH, Locator.response_text).send_keys(TestData.response_text)

        driver.find_element(By.XPATH, Locator.response_add_button).click()

        assert "/tickets/responses" in driver.current_url


        

        
