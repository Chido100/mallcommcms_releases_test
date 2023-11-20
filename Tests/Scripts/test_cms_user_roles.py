__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import TestData


class TestCMSUserRoles:

    def test_cms_user_roles(self, test_login):
        driver = test_login

        # Test CMS User Role
        driver.find_element(By.XPATH, Locator.manage_dropdown).click()
        sleep(2)

        # Hover and click on element
        cms_users = driver.find_element(By.XPATH, Locator.cms_users_dropdown)
        cms_user_roles = driver.find_element(By.XPATH, Locator.cms_user_roles)
        hover = ActionChains(driver).move_to_element(cms_users).move_to_element(cms_user_roles).click()
        hover.perform()

        role_name = driver.find_element(By.XPATH, Locator.cms_new_role_name)
        role_name.send_keys(TestData.cms_new_role_name)

        driver.find_element(By.XPATH, Locator.cms_role_submit_button).click()

        confirm = driver.find_element(By.XPATH, Locator.confirm_role_created)
        
        assert confirm.is_displayed()


