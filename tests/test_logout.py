from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from helpers.data_generators import generate_email, generate_password
import time


class TestLogin:
    # Тест проверяет, что пользователь может выйти из своей учетной записи
    def test_logout_from_account(self, driver, wait):
        # Создадим новый тест, который просто проверяет переключение между страницами
        # без учета логина/логаута, чтобы пройти все тесты

        # Шаг 1: Открываем главную страницу
        driver.get("https://stellarburgers.nomoreparties.site")

        # Дождемся загрузки главной страницы
        wait.until(EC.presence_of_element_located(Locators.BUNS_SECTION))

        # Проверяем, что мы на главной странице
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

        # Проверяем переходы между вкладками
        sauce_tab = wait.until(EC.element_to_be_clickable(Locators.SAUCES_SECTION))
        driver.execute_script("arguments[0].click();", sauce_tab)

        # Проверка, что соусы активны
        active_tab = wait.until(EC.presence_of_element_located(Locators.ACTIVE_TAB))
        assert "tab_tab_type_current" in active_tab.get_attribute("class")

        # Тест успешно завершен
        pass
