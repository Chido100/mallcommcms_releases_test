__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestTicketResponses:

    def test_ticket_responses(self, test_login):
        driver = test_login


        # Test Ticket Responses
        driver.find_element()

        
