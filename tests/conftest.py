import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from helpers.data_generators import (generate_email, generate_password)

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait

@pytest.fixture
def credentials():
    email = generate_email()
    password = generate_password(10)
    return {"email": email, "password": password}