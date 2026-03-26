import pytest
from selenium import webdriver

from pages.authPage import AuthPage
from pages.mainPage import MainPage
from pages.cartPage import CartPage
from pages.orderPage import OrderPage

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
    total = order_page.get_summary()
    assert total == "Total: $58.29"