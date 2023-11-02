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
        driver.find_element(By.XPATH, Locator.create_toggle_permission).click()
        # Click on Add Comment
        driver.find_element(By.XPATH, Locator.permission_add_comment).click()
        # Add comment in fields
        driver.find_element(By.XPATH, Locator.comment_title_1).send_keys(TestData.comment_1)
        driver.find_element(By.XPATH, Locator.comment_title_1).send_keys(TestData.comment_2)
        driver.find_element(By.XPATH, Locator.comment_title_1).send_keys(TestData.comment_3)
        # Click Add comment button
        driver.find_element(By.XPATH, Locator.permission_add_comment_button).click()
        # Click add permission button
        driver.find_element(By.XPATH, Locator.add_permissions_button).click()
        # Click View Log to check that permission is created
        driver.find_element(By.XPATH, Locator.view_log).click()
        driver.find_element(By.XPATH, Locator.view_log_close_button).click()


