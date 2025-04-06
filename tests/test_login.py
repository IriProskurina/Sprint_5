from locators.locators import Locators

class TestLogin:
    # Тест проверяет вход через главную страницу приложения
    def test_login_via_main_page(driver):
        # Шаг 1: Открыть страницу логина
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # Шаг 2: Ввести email и пароль
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys("example_user@example.com")
        driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys("ExamplePassword123")

        # Шаг 3: Нажать кнопку "Войти"
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # Шаг 4: Проверить, что пользователь успешно вошел
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "После успешного входа не произошел редирект на главную страницу"

    # Тест с использованием фикстуры авторизации
    def test_login_with_fixture(logged_in_user):
        # Проверяем, что пользователь успешно вошел и находится на главной странице
        assert logged_in_user.current_url == "https://stellarburgers.nomoreparties.site/", "Авторизация через фикстуру не привела к редиректу на главную страницу"
