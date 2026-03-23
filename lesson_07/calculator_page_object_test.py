import pytest
from selenium import webdriver

from pages.CalcPages import CalcPage

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
    calc_page.result_page()









