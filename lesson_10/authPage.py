from selenium.webdriver.common.by import By
import allure


class AuthPage:
    """
    Класс для взаимодействия со страницей авторизации интернет‑магазина.
    Предоставляет методы для ввода логина/пароля и выполнения входа в систему.
    """
    def __init__(self, driver):
        """
        Конструктор класса AuthPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    @allure.step("Ввод логина {value} в поле авторизации")
    def enter_login(self, value):
        """
        Вводит значение в поле "логин"

        :param value: str
        """
        username = self.driver.find_element(By.CSS_SELECTOR, "#user-name")
        username.send_keys(value)

    @allure.step("Ввод пароля {value} в поле авторизации")
    def enter_password(self, value):
        """
        Вводит значение в поле "пароль"

        :param value: str
        """
        psw = self.driver.find_element(By.CSS_SELECTOR, "#password")
        psw.send_keys(value)

    @allure.step("Нажатие кнопки входа («LOGIN»)")
    def click_button(self):
        """
        Нажимает на кнопку входа («LOGIN») на странице авторизации.

        """
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
