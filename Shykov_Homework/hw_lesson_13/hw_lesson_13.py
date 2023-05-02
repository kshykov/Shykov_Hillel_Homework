import csv

"""
Створіть функцію, яка повертає квадрати всіх чисел в діапазоні 0 - 100000
"""

def squares_in_range():
    return [i ** 2 for i in range(100000)]


squares = squares_in_range()
print(squares)

"""
Створіть функцію, яка читає файл csv. Вона приймає назву файлу(str), повертає список рядків(list). 
Також створіть функцію, яка записує в файл данні. Вона приймає назву файлу(str), список рядків(list),
 які треба записать в файл. Нічого не повертає. 
 Тепер за допомогою створених функцій спочатку створіть файл(3 рядків достатньо), потім прочитайте той-же файл, 
 записавши рядки в змінну, потім додайте два рядки в змінну, і після цього запишіть ваші зміни в інший файл.
"""

def read_csv(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        return [row for row in csv_reader]

def write_csv(file_name, rows):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(rows)

original_list =  [['Name', 'Age', 'Sex'],
                ['Ivam', 25, 'M'],
                ['Maria', 24, 'W']]

write_csv('users_iter_1', original_list)

read_file = read_csv("users_iter_1")

update_list = [['Slava', 28, 'M'],
            ['Emma', 22, 'W']]

update_file = original_list + update_list

write_csv('updated_file.csv', update_file)