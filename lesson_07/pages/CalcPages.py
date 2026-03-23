from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay_input_field(self, value):
        element = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        element.clear()
        element.send_keys(value)

    def press_buttons(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def result_page(self):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
            )
        # result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        # assert result == "15"