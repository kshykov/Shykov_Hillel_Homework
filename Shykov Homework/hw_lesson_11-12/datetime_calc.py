import datetime

"""
Реалізуйте функцію, яка додає або віднімає від заданої дати певну кількість днів.
 Приймає на вхід будь-яку дату та час (datetime), а також значення днів(int), 
 і знак(True або False, які репрезентують + і -). Повертає datetime. В цій задачі скористайтесь datetime.timedelta
"""






def add_or_subtract_days(date_time, days, add=''):
    if add == '+':
        return date_time + datetime.timedelta(days=days)
    elif add == '-':
        return date_time - datetime.timedelta(days=days)

date_time = datetime.datetime(2023, 4, 8)

# Додати 5 днів
add_date_time = add_or_subtract_days(date_time, 2, '+')
print(add_date_time)

# Відняти  днів
sub_date_time = add_or_subtract_days(date_time, 5, '-')
print(sub_date_time)

paskha = datetime.datetime(2023, 4, 15)
if add_date_time < paskha:
    print("Скоро вже буде пасха, так шо заказуйте мяско")