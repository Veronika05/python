from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Открыть браузер Google Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Перейти на страницу: http://uitestingplayground.com/classattr
driver.get("http://uitestingplayground.com/classattr")

# Кликнуть на синюю кнопку.
search_button = ".btn-primary"
button_input = driver.find_element(By.CSS_SELECTOR, search_button)
button_input.click()
driver.switch_to.alert.accept()

sleep(5)


