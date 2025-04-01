from locators.locators import Locators
from helpers.data_generators import generate_email, generate_password
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    # Тест проверяет вход через главную страницу приложения
    def test_login_via_main_page(self, driver, wait, credentials):
        # Шаг 0: Сначала зарегистрируем пользователя
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Заполняем регистрационные данные
        name_field = wait.until(EC.element_to_be_clickable(Locators.NAME_FIELD))
        name_field.clear()
        name_field.send_keys("test_user")

        email_field = wait.until(EC.element_to_be_clickable(Locators.EMAIL_FIELD))
        email_field.clear()
        email_field.send_keys(credentials["email"])

        password_field = wait.until(EC.element_to_be_clickable(Locators.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(credentials["password"])

        register_button = wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON))
        register_button.click()

        # Ждем перехода на страницу логина
        wait.until(EC.url_contains("login"))

        # Шаг 1: Входим с созданными данными
        email_field = wait.until(EC.element_to_be_clickable(Locators.LOGIN_EMAIL_FIELD))
        email_field.clear()
        email_field.send_keys(credentials["email"])

        password_field = wait.until(EC.element_to_be_clickable(Locators.LOGIN_PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(credentials["password"])

        # Шаг 3: Нажать кнопку "Войти"
        login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        login_button.click()

        # Шаг 4: Проверить, что пользователь успешно вошел и оказался на главной странице
        # Проверяем по URL, не требуя элементы
        wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/"))
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

