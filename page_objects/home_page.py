from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.XPATH, "//input[@name='name']")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.ID, "exampleInputPassword1")
    icecream_checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpwd(self):
        return self.driver.find_element(*HomePage.password)

    def check_icecream(self):
        return self.driver.find_element(*HomePage.icecream_checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submit_btn(self):
        return self.driver.find_element(*HomePage.submit)

    def  get_message(self):
        return self.driver.find_element(*HomePage.success_message)


