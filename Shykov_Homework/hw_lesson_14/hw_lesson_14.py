import random

"""
Створіть декоратор, який виводить в консоль ім'я функції, яку було ввикликано.
Наприклад, створіть пару функцій для аріфметичних операцій додавання і множення.
При виклику цих функцій має повертатись результат операції і виводиться в консоль ім'я функції, яку було ввикликано.
"""


def func_name(func):
    def inner(*args, **kwargs):
        print(f'Було використано функцію {func.__name__}')
        return func(*args, **kwargs)
    return inner
@func_name
def add(a, b):
    return a + b
@func_name
def multiply(a, b):
    return a * b

print(add(2, 2))
print(multiply(4, 4))

"""
Створіть за допомогою list comprehension список, в якому буде 100 елементів, 
і кожен із яких буде в границях від 1 до 10 (для цього можна скористатись функцією randint із модуля random). 
Порахуйте кількість кожного елемента і виведіть в консоль
"""

random_numbers = [random.randint(1, 10) for _ in range(100)]

for element in range(1, 11):
    count = random_numbers.count(element)
    print(f"Число {element} зустрічається {count} разів")