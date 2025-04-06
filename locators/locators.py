from selenium.webdriver.common.by import By

class Locators:

    # Регистрация
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]") # Кнопка "Зарегистрироваться"
    NAME_FIELD = (By.XPATH, "//fieldset[1]//input") # Поле ввода имени
    EMAIL_FIELD = (By.XPATH, "//fieldset[2]//input") # Поле ввода email
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']") # Поле ввода пароля
    REGISTRATION_ERROR = (By.XPATH, "//p[contains(@class, 'input__error') and contains(text(), 'Некорректный пароль')]") # Ошибка при некорректной регистрации

    # Логин
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]") # Кнопка "Войти"
    LOGIN_EMAIL_FIELD = (By.XPATH, "//fieldset[1]//input")  # Поле email для входа
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")  # Поле пароля для входа
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")  # Кнопка "Личный кабинет"

    # Навигация
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") #Конструктор
    LOGO = (By.XPATH, "//a[@href='/']")  # Логотип Stellar Burgers

    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")  # Кнопка "Выход"

    # Конструктор
    BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab')]//span[text()='Булки']")  # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab')]//span[text()='Соусы']")  # Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab')]//span[text()='Начинки']") # Раздел "Начинки"
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]") # Активная вкладка (по классу)
