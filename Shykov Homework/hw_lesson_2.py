from math import pi

# Task 1
first_name = input("You are welcome!\n Please enter your first name")
last_name = input("Please enter your last name")
full_name = first_name + " " + last_name

# Subtask 1
print(full_name)

# Subtask 2
print(full_name.lower() + " " + full_name.upper() + " " + full_name.title())

# Subtask 3
name_multiplied = (full_name.title() + " ") * 5
print(name_multiplied)

# Task 2

radius = float(input("Введіть радіус кола"))

circle_len = 2 * pi * radius
circle_sqr = pi * radius**2

print(f"Довжина кола з радіусом {radius} дорівнює {circle_len.__round__(3)}")
print(f"Площа кола з радіусом {radius} дорівнює {circle_sqr.__round__(3)}")

# Task 3

currency_rate = float(input("Введіть поточний курс валюти"))
exchange_amount = float(input("Введдіть сумму яку хочете обміняти"))
to_be_issued_amount = exchange_amount * currency_rate

print(f"При обміні {exchange_amount.__round__(2)} по курсу {currency_rate.__round__(2)} ви отримаєте"
      f" {to_be_issued_amount.__round__(2)}"
)
