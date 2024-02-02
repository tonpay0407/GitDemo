from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver

    register_btn = (By.XPATH, "//a[contains(text(),'Register')]")

    def registerbtn_func(self):
        return self.driver.find_element(*Login.register_btn)

