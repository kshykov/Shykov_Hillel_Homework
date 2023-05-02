"""
Реалізуйте функцію, яка вираховує ваш точний вік(не обов'язково вказувати свої данні),
вираховуючі різницю між наданим значеням і значенням datetime.now(). Приймає дату та час(datetime),
повертає два значення: datetime і datetime.timestamp.
В цій задачі скористайтесь для конвертації datetime.timestamp. Виведіть результат в консоль

"""
import datetime


def calculate_exact_age(birth_date_time):
    now = datetime.datetime.now()
    age = now - birth_date_time

    return age

birth_date_time = datetime.datetime(1995, 3, 20)

age = calculate_exact_age(birth_date_time)

print("Вік у вигляді datetime:", age)

