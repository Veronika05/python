import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()

def test_swag_labs(browser):
    browser.get("https://www.saucedemo.com/")

    username = browser.find_element(By.CSS_SELECTOR, "#user-name")
    username.send_keys("standard_user")

    psw = browser.find_element(By.CSS_SELECTOR, "#password")
    psw.send_keys("secret_sauce")

    button = browser.find_element(By.CSS_SELECTOR, "#login-button").click()

    shop_1 = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    shop_2 = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    shop_3 = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    cart_link = browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    checkout = browser.find_element(By.CSS_SELECTOR, "#checkout").click()

    first_name = browser.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.send_keys("Veronika")

    last_name = browser.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("Barhonova")

    code = browser.find_element(By.CSS_SELECTOR,"#postal-code")
    code.send_keys("429147")

    cont = browser.find_element(By.CSS_SELECTOR,"#continue").click()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".summary_total_label")))

    total = browser.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    
    assert total == "Total:$58.29"