__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestVirtualOnboarding:

    def test_virtual_onboarding(self, test_login):
        driver = test_login


        # Test Vitual Onboarding
        driver.find_element(By.XPATH, Locator.people_dropdown).click()
        driver.find_element(By.XPATH, Locator.virtual_onboarding).click()

        driver.find_element(By.XPATH, Locator.invite_new_contact).click()
        driver.find_element(By.XPATH, Locator.vo_first_name).send_keys(TestData.vo_first_name)
        driver.find_element(By.XPATH, Locator.vo_last_name).send_keys(TestData.vo_last_name)
        driver.find_element(By.XPATH, Locator.vo_email_address).send_keys(TestData.vo_email_address)

        driver.find_element(By.XPATH, Locator.vo_invite_button).click()

        assert driver.find_element(By.XPATH, Locator.invite_success_alert).is_displayed()
        

        
