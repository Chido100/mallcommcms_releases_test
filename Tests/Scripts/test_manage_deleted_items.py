__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestManageDeletedItems:

    def test_manage_deleted_items(self, test_login):
        driver = test_login
        