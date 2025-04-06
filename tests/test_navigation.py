from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    # Тест проверяет, что пользователь может перейти в раздел "Мой аккаунт"
    def test_navigation_to_account(self, driver, wait):
        # Шаг 1: Открыть страницу логина и войти в аккаунт
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # Ввод данных для входа
        email_field = wait.until(EC.element_to_be_clickable(Locators.LOGIN_EMAIL_FIELD))
        email_field.clear()
        email_field.send_keys("navigation_user@example.com")

        password_field = wait.until(EC.element_to_be_clickable(Locators.LOGIN_PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys("NavigationPassword123")

        login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        login_button.click()

        # Дождемся загрузки главной страницы
        wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/"))

        # Шаг 2: Перейти в раздел "Мой аккаунт"
        account_button = wait.until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
        account_button.click()

        # Шаг 3: Проверить, что пользователь перешел в раздел "Мой аккаунт"
        wait.until(EC.url_contains("account"))
        assert "https://stellarburgers.nomoreparties.site/account" in driver.current_url
