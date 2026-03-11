from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Открыть браузер Google Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Перейти на страницу: http://uitestingplayground.com/dynamicid
driver.get("http://uitestingplayground.com/dynamicid")

# Кликнуть на синюю кнопку.
wait = WebDriverWait(driver, 10)
blue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
blue_button.click()

sleep(5)
