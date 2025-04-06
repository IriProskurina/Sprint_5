import random
import string


def generate_email(domain="gmail.com"):
    """
    Генерирует email в формате: имя_фамилия_номер когорты_любые 3 цифры@домен
    Например: ivan_petrov_cohort123_456@gmail.com
    """
    names = ["ivan", "petr", "anna", "elena", "maxim", "olga", "sergey", "natalia"]
    surnames = ["petrov", "ivanov", "sidorov", "kuznetsov", "smirnov", "popov", "sokolov", "novikov"]

    name = random.choice(names)
    surname = random.choice(surnames)
    cohort_number = f"cohort{random.randint(1, 999)}"
    three_digits = ''.join(random.choices(string.digits, k=3))

    return f"{name}_{surname}_{cohort_number}_{three_digits}@{domain}"


def generate_password(length=8):
    if length < 4:
        raise ValueError("Пароль должен быть не менее 4 символов.")
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))