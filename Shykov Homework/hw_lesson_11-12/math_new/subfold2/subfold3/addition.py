def add(a, b):
    try:
        return a + b
    except TypeError:
        print(f"Так не можна робити! перевірте вхідні дані")
        return ''