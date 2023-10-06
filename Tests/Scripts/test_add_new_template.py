__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestAddNewTemplate:

    def test_add_new_template(self, test_login):
        driver = test_login


        # Add new template
