import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):

    service_object = Service()
    driver = webdriver.Chrome(service=service_object)
    driver.get("https://rahulshettyacademy.com/client")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


