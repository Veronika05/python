import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_swag_labs(driver):
    
    auth_page = AuthPage(driver)
    auth_page.enter_login("standard_user")
    auth_page.enter_password("secret_sauce")
    auth_page.click_button()

    main_page = MainPage(driver)
    main_page.add_to_cart()
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    order_page = OrderPage(driver)
    order_page.fill_name("Veronika")
    order_page.fill_last_name("Barhonova")
    order_page.fill_code("429147")
    order_page.click_cont()
