
# Task 1
# Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому,
# так і другому списках, і надрукуйте їх у порядку зростання.

set_1 = {60, 4, 3, 10, 20, 1}
set_2 = {60, 2, 3, 40, 30, 1}

print(set_1.intersection(set_2))

# Task 2 Створіть словник із даними про студентів: ключі - імена студентів, значення - бали для кожного.
# Програма повинна визначити середній бал і вивести імена студентів, чий бал вище середнього.

students = {
    "Student_1": 100,
    "Student_2": 95,
    "Student_3": 1,
    "Student_4": 59
}

avarage = sum(students.values()) / len(students)

for student in students.keys():
    if students[student] > avarage:
        print(student)

# Task 3 Даний список цілих чисел. Визначте кількість різних значень.

set_1 = {60, 4, 3, 10, 20, 1, 60, 2, 3, 40, 30, 1}

print(f"Кількість різних значень становить {len(set_1)}")


# Task 4 Дано два списки чисел. Виведіть всі числа, які входять як в перший, так і в другий список в порядку зростання.
# Вводяться два списки цілих чисел. Всі числа кожного списку знаходяться на окремому рядку.

list_1 = [60, 4, 3, 10, 20, 1]
list_2 = [60, 2, 3, 40, 30, 1]

set1 = set(list_1)
set2 = set(list_2)
set_inter = set1.intersection(set2)

for element in set_inter:
    print(element)

for element in set1:
    print(element)

for element in set2:
    print(element)


#  Task 5

text = "one two three one four five seven ten seven one"
words = text.split()

list_key = list(range(0, 100))

dict1 = dict(zip(list_key, words))

for key, value in dict1.items():
    x = key, value
    print(x)