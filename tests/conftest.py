import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from helpers.data_generators import (generate_email, generate_password)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)  # явное ожидание до 15 секунд

@pytest.fixture
def credentials():
    email = generate_email()
    password = generate_password(10)
    return {"email": email, "password": password}


@pytest.fixture
def logged_in_user(driver, wait):
    """Фикстура для входа пользователя в аккаунт"""
    # Открыть страницу логина
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Ввести email и пароль
    driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys("example_user@example.com")
    driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys("ExamplePassword123")

    # Нажать кнопку "Войти"
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Дождаться загрузки главной страницы
    wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/"))

    return driver