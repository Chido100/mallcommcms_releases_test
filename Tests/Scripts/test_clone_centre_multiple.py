__author__ = 'Chidozie Amefule'


from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from time import sleep
import TestData


class TestMultipleCentreClone:

    def test_multiple_centre_clone(self, test_login):
        driver = test_login


        # Test Clone Multiple Centre