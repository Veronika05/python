import pytest
from selenium import webdriver
import allure

from authPage import AuthPage
from mainPage import MainPage
from cartPage import CartPage
from orderPage import OrderPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@allure.title("Тестирование интернет-магазина")
@allure.description("Авторизация → добавление товаров в корзину → оформление заказа → проверка итоговой суммы")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_swag_labs(driver):
    with allure.step("Авторизация на сайте"):
        auth_page = AuthPage(driver)
        with allure.step("Ввод логина: standard_user"):
            auth_page.enter_login("standard_user")
        with allure.step("Ввод пароля: secret_sauce"):
            auth_page.enter_password("secret_sauce")
        with allure.step("Нажатие кнопки входа"):
            auth_page.click_button()

    with allure.step("Добавление товаров в корзину"):
        main_page = MainPage(driver)
        with allure.step("Добавление 3-х товаров в корзину"):
            main_page.add_to_cart()
        with allure.step("Переход в корзину"):
            main_page.go_to_cart()

    with allure.step("Начало оформления заказа"):
        cart_page = CartPage(driver)
        with allure.step("Нажатие кнопки Checkout"):
            cart_page.click_checkout()

    with allure.step("Заполнение данных для оформления заказа"):
        order_page = OrderPage(driver)
        with allure.step("Заполнение имени: Veronika"):
            order_page.fill_name("Veronika")
        with allure.step("Заполнение фамилии: Barhonova"):
            order_page.fill_last_name("Barhonova")
        with allure.step("Заполнение почтового кода: 429147"):
            order_page.fill_code("429147")
        with allure.step("Нажатие кнопки Continue"):
            order_page.click_cont()

    with allure.step("Шаг 5: Проверка итоговой суммы заказа"):
        total = order_page.get_summary()
        with allure.step(f"Проверка итоговой суммы: ожидается 'Total: $58.29', получено '{total}'"):
            assert total == "Total: $58.29"
