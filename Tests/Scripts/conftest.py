import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Drivers.drivers import driver_service
from time import sleep
import datetime
from Tests.PageObject.Locators import Locator
import TestData



@pytest.fixture   
def test_login():

        # Setup Environment
        driver = webdriver.Chrome(service=driver_service)
        driver.set_window_size(1240, 1080)
        driver.get("https://release-cms.mallcomm.co.uk/")
        driver.implicitly_wait(20)

        print('Run started at : ' + str(datetime.datetime.now()))
        print('Test Environment Set Up')
        print('-----------------------')
        

        # login procedure
        enter_email = driver.find_element(By.XPATH, Locator.login_email)
        enter_email.clear()
        enter_email.send_keys(TestData.valid_email)
        driver.find_element(By.XPATH, Locator.login_next_button).click()
        sleep(2)

        driver.find_element(By.XPATH, Locator.login_with_toolbox).click()

        print_email = driver.find_element(By.XPATH, Locator.print_email)
        print_email.send_keys(TestData.valid_email)
        driver.find_element(By.XPATH, Locator.print_email_next_button).click()

        print_password = driver.find_element(By.XPATH, Locator.print_password)
        print_password.send_keys(TestData.password)
        sleep(2)

        driver.find_element(By.XPATH, Locator.print_password_next_button).click()
        sleep(2)

        driver.find_element(By.XPATH, Locator.select_database).click()
        yield driver

        # TearDown Environment
        print('---------------------')
        print('Test Environment Destroyed')
        print('Run Completed at: ' + str(datetime.datetime.now()))
        driver.close()
        driver.quit()  
