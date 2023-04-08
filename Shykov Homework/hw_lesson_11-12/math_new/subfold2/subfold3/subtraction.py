def subtract(a, b):
    try:
        return a - b
    except TypeError:
        print(f"Тут теж так не можна робити! перевірте вхідні дані")
        return ''