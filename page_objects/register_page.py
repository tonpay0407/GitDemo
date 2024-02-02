from selenium.webdriver.common.by import By


class Register:

    def __init__(self,driver):
        self.driver = driver


    firstName = (By.XPATH, "//input[@id='firstName']")
    # put this in tuple
    lastName = (By.ID, "lastName")

    def firstname(self):
        return self.driver.find_element(*Register.firstName)

    def lastname_func(self):
        return self.driver.find_element(*Register.lastName)
