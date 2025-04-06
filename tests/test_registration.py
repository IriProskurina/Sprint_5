import pytest
from helpers.data_generators import generate_email, generate_password
from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:
    # Тест проверяет успешную регистрацию нового пользователя
    def test_successful_registration(self, driver, wait):
        # Шаг 1: Открыть страницу регистрации
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Генерация случайных данных
        random_email = generate_email()
        random_password = generate_password(8)

        # Шаг 2: Ввести имя, email и пароль
        name_field = wait.until(EC.element_to_be_clickable(Locators.NAME_FIELD))
        name_field.clear()
        name_field.send_keys("test_user")

        email_field = wait.until(EC.element_to_be_clickable(Locators.EMAIL_FIELD))
        email_field.clear()
        email_field.send_keys(random_email)

        password_field = wait.until(EC.element_to_be_clickable(Locators.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(random_password)

        # Шаг 3: Нажать кнопку "Зарегистрироваться"
        register_button = wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON))
        register_button.click()

        # Шаг 4: Проверить, что произошел переход на страницу логина
        wait.until(EC.url_contains("login"))
        assert "login" in driver.current_url

    # Тест проверяет, что при вводе некорректного пароля появляется ошибка
    def test_registration_invalid_password(self, driver, wait):
        # Шаг 1: Открыть страницу регистрации
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Шаг 2: Ввести имя, email и некорректный пароль
        name_field = wait.until(EC.element_to_be_clickable(Locators.NAME_FIELD))
        name_field.clear()
        name_field.send_keys("invalid_user")

        email_field = wait.until(EC.element_to_be_clickable(Locators.EMAIL_FIELD))
        email_field.clear()
        email_field.send_keys("invalid_user@example.com")

        password_field = wait.until(EC.element_to_be_clickable(Locators.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys("123")

        # Шаг 3: Нажать кнопку "Зарегистрироваться"
        register_button = wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON))
        register_button.click()

        # Шаг 4: Проверить, что появилась ошибка "Некорректный пароль"
        error_message = wait.until(EC.visibility_of_element_located(Locators.REGISTRATION_ERROR)).text
        assert "Некорректный пароль" in error_message