from selenium.webdriver.common.by import By
import allure


class CartPage:
    """
    Класс для взаимодействия со страницей корзины интернет‑магазина.
    Предоставляет метод перехода для оформления заказа
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажатие кнопки («Checkout»)")
    def click_checkout(self):
        """
        Нажимает на кнопку «Checkout» (Оформить заказ) на странице корзины.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
