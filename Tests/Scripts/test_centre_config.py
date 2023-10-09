__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import TestData


class TestCentreConfig:

    def test_centre_config(self, test_login):
        driver = test_login


        # Test Centre Config
        driver.find_element(By.XPATH, Locator.manage_dropdown).click()
        sleep(2)

        # Hover and click on element
        system_config = driver.find_element(By.XPATH, Locator.system_config_dropdown)
        centre_config = driver.find_element(By.XPATH, Locator.centre_config)
        hover = ActionChains(driver).move_to_element(system_config).move_to_element(centre_config).click()
        hover.perform()

        assert "manage/centre-config/" in driver.current_url

        

