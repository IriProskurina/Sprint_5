import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators

class TestLogin:
    # Тест проверяет вход в систему с использованием заранее сгенерированных данных.
    def test_login_with_generated_credentials(driver, credentials, wait):
        # Шаг 1: Открыть страницу логина
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # Шаг 2: Ввести email и пароль
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(credentials["email"])  # Используем переданные сгенерированные email
        driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys(credentials["password"])  # Используем переданные сгенерированные пароль

        # Шаг 3: Нажать кнопку "Войти"
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # Шаг 4: Проверить, что произошел успешный вход (пользователь оказался на главной странице)
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

        # Шаг 4: Проверить, что произошел успешный вход (пользователь оказался на главной странице)
        wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/"))
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url
        # Шаг 4: Проверить, что произошел успешный вход (пользователь оказался на главной странице)
        wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/"))
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_urls