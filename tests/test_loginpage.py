from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from page_objects.login_page import Login
from page_objects.register_page import Register
from utility.baseclass import BaseClass



class TestOne(BaseClass):

    def test_login_logo (self, setup):
        print("running tests")
        self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Log')]")

    def test_registration(self):
        login = Login(self.driver)
        login.registerbtn_func().click()
        register = Register(self.driver)
        register.firstname().send_keys("Abhishek")
        register.lastname_func().send_keys("Sharma")




