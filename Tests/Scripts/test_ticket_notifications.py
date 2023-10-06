__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestTicketNotification:

    def test_ticket_notification(self, test_login):
        driver = test_login
        
        
