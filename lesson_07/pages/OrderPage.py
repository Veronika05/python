from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
    def __init__(self, driver):
        self.driver = driver


    def fill_name(self, value):
        first_name = self.driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name.send_keys(value)
    
    def fill_last_name(self, value):
        last_name = self.driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name.send_keys(value)

    def fill_code(self, value):
        code = self.driver.find_element(By.CSS_SELECTOR,"#postal-code")
        code.send_keys(value)

    def click_cont(self):
        cont = self.driver.find_element(By.CSS_SELECTOR,"#continue").click()

    def get_summary(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,".summary_total_label"))
            )

        total = self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text

        assert total == "Total: $58.29"