from selenium.webdriver.common.by import By

class AuthPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def enter_login(self, value):
        username = self.driver.find_element(By.CSS_SELECTOR, "#user-name")
        username.send_keys(value)

    def enter_password(self, value):
        psw = self.driver.find_element(By.CSS_SELECTOR, "#password")
        psw.send_keys(value)

    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()