import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay.clear()
    delay.send_keys("45")
    button_1 = browser.find_element(By.XPATH, "//span[text()='7']").click()
    button_2 = browser.find_element(By.XPATH, "//span[text()='+']").click()
    button_3 = browser.find_element(By.XPATH, "//span[text()='8']").click()
    button_4 = browser.find_element(By.XPATH, "//span[text()='=']").click()
    
    result = WebDriverWait(browser, 50).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
)
    assert result