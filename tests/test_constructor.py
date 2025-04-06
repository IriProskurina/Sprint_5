from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class TestConstructorTabs:
    # Тест проверяет, что при выборе вкладки "Булки" она становится активной
    def test_constructor_buns_tab(driver, wait):
        # Шаг 1: Открыть главную страницу
        driver.get("https://stellarburgers.nomoreparties.site")

        # Шаг 2: Нажать на вкладку "Булки"
        driver.find_element(*Locators.BUNS_SECTION).click()

        # Шаг 3: Проверить, что вкладка активна
        wait.until(EC.visibility_of_element_located(Locators.ACTIVE_TAB))
        is_buns_active = driver.find_element(*Locators.ACTIVE_TAB).get_attribute("class")
        assert "tab_tab_type_current" in is_buns_active, "Ожидалось, что вкладка 'Булки' станет активной, но этого не произошло"

    # Тест проверяет, что при выборе вкладки "Соусы" она становится активной
    def test_constructor_sauces_tab(driver, wait):
        # Шаг 1: Открыть главную страницу
        driver.get("https://stellarburgers.nomoreparties.site")

        # Шаг 2: Нажать на вкладку "Соусы"
        driver.find_element(*Locators.SAUCES_SECTION).click()

        # Шаг 3: Проверить, что вкладка активна
        wait.until(EC.visibility_of_element_located(Locators.ACTIVE_TAB))
        is_sauces_active = driver.find_element(*Locators.ACTIVE_TAB).get_attribute("class")
        assert "tab_tab_type_current" in is_sauces_active, "Ожидалось, что вкладка 'Соусы' станет активной, но этого не произошло."

    # Тест проверяет, что при выборе вкладки "Начинки" она становится активной
    def test_constructor_fillings_tab(driver, wait):
        # Шаг 1: Открыть главную страницу
        driver.get("https://stellarburgers.nomoreparties.site")

        # Шаг 2: Нажать на вкладку "Начинки"
        driver.find_element(*Locators.FILLINGS_SECTION).click()

        # Шаг 3: Проверить, что вкладка активна
        wait.until(EC.visibility_of_element_located(Locators.ACTIVE_TAB))
        is_fillings_active = driver.find_element(*Locators.ACTIVE_TAB).get_attribute("class")
        assert "tab_tab_type_current" in is_fillings_active, "Ожидалось, что вкладка 'Начинки' станет активной, но этого не произошло."