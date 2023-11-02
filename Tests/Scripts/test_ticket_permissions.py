__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestTicketPermissions:

    def test_ticket_permissions(self, test_login):
        driver = test_login

    
        # Test Ticket Permissions
        driver.find_element(By.XPATH, Locator.manage_dropdown).click()
        driver.find_element(By.XPATH, Locator.ticket_permissions).click()
        
        # Turn on some toggles
        # Click on Add Comment
        # Add comment in fields
        # Click Add comment button
        # Click add permission button
        driver.find_element(By.XPATH, Locator.add_permissions_button).click()
        # Click View Log to check that permission is created
        

