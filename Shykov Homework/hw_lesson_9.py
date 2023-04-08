"""
Напишіть програму яка перевіряє чи стрічка містить лише великі і малі літери, числа на нижнє підкреслення.

Напишіть програму, що видаляє область дужок в стрічці

["example (.com)", "github (.com)", "stackoverflow (.com)"] ->
"""

import re

def validate_string(s):
    pattern = "^[A-Za-z0-9_]*$"
    return bool(re.match(pattern, s))

def remove_brackets(s):
    pattern = r'\s*\([^)]*\)'
    return re.sub(pattern, '', s)

# Приклад використання
strings = ["example (.com)", "github (.com)", "stackoverflow (.com)"]

for s in strings:
    s = remove_brackets(s)
    if validate_string(s):
        print(s)

