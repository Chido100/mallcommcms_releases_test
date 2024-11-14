__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData
from selenium.webdriver.common.action_chains import ActionChains
from imagefiles import profile_image


class TestAddCMSUser:

    def test_add_cms_user(self, test_login):
        driver = test_login


        # Add CMS User
        driver.find_element(By.XPATH, Locator.manage_dropdown).click()
        sleep(2)

        # Hover and click on element
        users_d = driver.find_element(By.XPATH, Locator.cms_users_dropdown)
        all_users = driver.find_element(By.XPATH, Locator.all_cms_users)
        hover = ActionChains(driver).move_to_element(users_d).move_to_element(all_users).click()
        hover.perform()

        driver.find_element(By.XPATH, Locator.add_cms_user_button).click()

        add_firstname = driver.find_element(By.XPATH, Locator.add_cms_first_name)
        add_firstname.send_keys(TestData.cms_user_firstname)

        add_lastname = driver.find_element(By.XPATH, Locator.add_cms_last_name)
        add_lastname.send_keys(TestData.cms_user_lastname)

        add_email = driver.find_element(By.XPATH, Locator.add_cms_email)
        add_email.send_keys(TestData.cms_user_email)

        driver.find_element(By.XPATH, Locator.add_cms_role_toggle).click()
        driver.find_element(By.XPATH, Locator.add_cms_user_create_button).click()
        sleep(2)

        assert driver.find_element(By.XPATH, Locator.add_cms_user_success).is_displayed()

