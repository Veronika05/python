import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    yield driver
    driver.quit()

def test_form(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    first_name = browser.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")
    last_name = browser.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")
    address = browser.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")
    email = browser.find_element(By.NAME, "e-mail")
    email.send_keys("test@skypro.com")
    phone_number = browser.find_element(By.NAME, "phone")
    phone_number.send_keys("+7985899998787")
    city = browser.find_element(By.NAME, "city")
    city.send_keys("Москва")
    country = browser.find_element(By.NAME, "country")
    country.send_keys("Россия")
    job_position = browser.find_element(By.NAME, "job-position")
    job_position.send_keys("QA")
    company = browser.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

#нажать submit
    browser.find_element(By.CSS_SELECTOR, 'button').click()

    #ждем .alert
    wait = WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))
    
    element = browser.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute('class')

    assert "alert-danger" in element, f'Пришел {element}'

    elements = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]

    for e in elements:
        element = browser.find_element(By.CSS_SELECTOR, f'#{e}')
        class_atr = element.get_attribute('class') or ''
        assert "alert-success" in class_atr

    browser.quit()



















