__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestManageAccessLevel:

    def test_manage_access_level(self, test_login):
        driver = test_login

        
