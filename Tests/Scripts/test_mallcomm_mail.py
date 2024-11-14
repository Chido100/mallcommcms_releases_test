__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestMallcommMail:

    def test_mallcomm_mail(self, test_login):
        driver = test_login

        # Create a mail thread
        driver.find_element(By.XPATH, Locator.items_dropdown).click()
        driver.find_element(By.XPATH, Locator.mallcomm_mail).click()

        # Add new thread
        driver.find_element(By.XPATH, Locator.add_new_thread_button).click()
        driver.find_element(By.XPATH, Locator.mail_recipient_store).click()
        driver.find_element(By.XPATH, Locator.mail_recipient_selected_store).click()

        driver.find_element(By.XPATH, Locator.mail_recipient_receiver).click()
        driver.find_element(By.XPATH, Locator.mail_recipient_selected_receiver).click()

        driver.find_element(By.XPATH, Locator.mail_select_button).click()
        driver.find_element(By.XPATH, Locator.mail_selected_button).click()

        subject = driver.find_element(By.XPATH, Locator.mail_subject)
        subject.send_keys(TestData.mm_subject)

        message = driver.find_element(By.XPATH, Locator.mail_message)
        message.send_keys(TestData.mm_message)

        driver.find_element(By.XPATH, Locator.add_mail_message_button).click()

        assert "/mmail/" in driver.current_url



        
