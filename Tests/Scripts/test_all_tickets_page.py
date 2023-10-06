__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestAllTickets:

    def test_all_tickets(self, test_login):
        driver = test_login

        # All Tickets Page Test
        driver.find_element(By.XPATH, Locator.ticketing_dropdown).click()
        driver.find_element(By.XPATH, Locator.all_tickets).click()

        assert driver.find_element(By.XPATH, Locator.check_all_ticket).is_displayed()
