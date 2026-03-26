import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.calcPages import CalcPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_calculator(driver):

    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.delay_input_field("45")
    calc_page.press_buttons()
    result = calc_page.result_page()
    assert result == "15"









