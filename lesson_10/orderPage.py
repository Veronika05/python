from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrderPage:
    """
        Класс для взаимодействия со страницей оформления заказа.
        Предоставляет методы для заполнения полей формы и получения итоговой суммы.
    """
    def __init__(self, driver):
        """
        Конструктор класса OrderPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Заполнение поля «Имя» значением {value}")
    def fill_name(self, value):
        """
        Заполняет поле "имя"

        :param value: str - Имя пользователя, которое нужно ввести в поле
        """
        first_name = self.driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name.send_keys(value)

    @allure.step("Заполнение поля «Фамилия» значением {value}")
    def fill_last_name(self, value):
        """
        Заполняет поле "фамилия"

        :param value: str - Фаимилия пользователя, которое нужно ввести в поле
        """
        last_name = self.driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name.send_keys(value)

    @allure.step("Заполнение поля «Почтовый индекс» значением {value}")
    def fill_code(self, value):
        """
        Заполняет поле "почтовый индекс"

        :param value: str - Почтовый код, который нужно ввести в поле.
        """
        code = self.driver.find_element(By.CSS_SELECTOR, "#postal-code")
        code.send_keys(value)

    @allure.step("Нажатие кнопки «Продолжить» (Continue)")
    def click_cont(self):
        """
        Нажимает на кнопку «Продолжить» (Continue) на странице оформления заказа.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    @allure.step("Получение текста итоговой суммы из блока подтверждения заказа")
    def get_summary(self):
        """
        Получает текст итоговой суммы из блока подтверждения заказа.

        Ожидает видимости элемента с итоговой суммой, затем возвращает его текстовое содержимое.

        :return: str — текст итоговой суммы
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
            )

        return self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
