from locators.locators import Locators


class TestLogout:
    # Тест проверяет, что пользователь может выйти из своей учетной записи
    def test_logout_from_account(logged_in_user, driver):
        driver = logged_in_user

        # Перейти в раздел "Мой аккаунт" и нажать "Выйти"
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        # Проверить, что пользователь вернулся на страницу входа
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "После выхода из аккаунта не произошел редирект на страницу входа"