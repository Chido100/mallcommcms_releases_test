__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestManageCentreTags:

    def test_manage_centre_tags(self, test_login):
        driver = test_login

        
