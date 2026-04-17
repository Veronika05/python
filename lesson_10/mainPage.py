from selenium.webdriver.common.by import By
import allure


class MainPage:
    """
    Класс для взаимодействия с главной страницей интернет‑магазина.
    Предоставляет методы для добавления товаров в корзину и перехода в корзину.
    """
    def __init__(self, driver):
        """
        Конструктор класса MainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Добавить товары в корзину")
    def add_to_cart(self):
        """
        Добавляет товары в корзину
        """
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переход в корзину через иконку корзины")
    def go_to_cart(self):
        """
        Осуществляет переход в корзину
        """
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
