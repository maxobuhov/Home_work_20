# Home_work_20
Моя домашняя работа под номером 20


Необходимо создать 
оо
import csv
def password_validator(length: int = 8, uppercase: int = 1, lowercase: int = 1, special_chars: int = 1):
"""
Декоратор для валидации паролей.
Параметрыр:
length (int): Минимальная длина пароля (по умолчанию 8).
uppercase (int): Минимальное количество букв верхнего регистра (по умолчанию 1).
lowercase (int): Минимальное количество букв нижнего регистра (по умолчанию 1).
special_chars (int): Минимальное количество спец-знаков (по умолчанию 1).
Пример использования:
@password_validator(length=10, uppercase=2, lowercase=2, special_chars=2)
def register_user(username: str, password: str):
pass
"""
def username_validator():
pass
@password_validator(length=10, uppercase=2, lowercase=2, special_chars=2)
@username_validator
def register_user(username: str, password: str):
"""
Функция для регистрации нового пользователя.
Параметры:
username (str): Имя пользователя.
password (str): Пароль пользователя.
Raises:
ValueError: Если пароль или юзернейм не соответствует заданным условиям.
"""
# Запись имени пользователя и пароля в CSV файл