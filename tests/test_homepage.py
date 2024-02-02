import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

from page_objects.home_page import HomePage
from test_data.homepage_data import HomePageData
from utility.baseclass import BaseClass


class TestHomePage(BaseClass):

    @pytest.mark.usefixtures("get_data")
    def test_formsubmission(self, get_data):
        log = self.getLogger()
        newservice_obj = Service()
        driver = webdriver.Chrome(service=newservice_obj)
        driver.get('https://rahulshettyacademy.com/angularpractice/')
        homepage_obj = HomePage(driver)
        log.info('Enetered test')
        homepage_obj.getname().send_keys(get_data['name'])
        homepage_obj.getemail().send_keys(get_data['email'])
        homepage_obj.getpwd().send_keys(get_data['pwd'])
        homepage_obj.check_icecream().click()
        Sel = Select(homepage_obj.getGender())
        Sel.select_by_visible_text(get_data['gender'])
        homepage_obj.submit_btn().click()
        log.info('Submit has been clicked')
        text = homepage_obj.get_message().text

        assert "Success!" in text

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def get_data(self, request):
        return request.param


