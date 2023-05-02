"""
1.Користувач вводить сторони опуклого чотирикутника.

  Якщо це прямокутник, програма знаходить його площу (це виконують дві окремі функції)
  Якщо це квадрат, програма повідомляє про це користувача (це перевіряє окрема функція)
  На зчитування введеного користувачем значення сторони теж рекомендую зробити функцію

Підказка1: серед опуклих чотирикутників, лише у прямокутників та квадратів діагоналі дорівнюють та
утворюють прямокутний трикутник. Це можна перевірити, використовуючи теорему Піфагора.

підказка2: опуклий чотирикутник є прямокутником, якщо сума квадратів його перших двох сторін
дорівнює сумі квадратів його останніх двох сторін.
"""
print("Введіть сторони позначені на схемі"
      "\n|‾‾‾‾‾‾‾‾‾‾‾‾‾A‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n"
      "|                              |\n"
      "|                              |\n"
      "B                              D\n"
      "|                              |\n"
      "|                              |\n"
      "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾C‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

side_a = float(input("Enter Side A: "))
side_b = float(input("Enter Side B: "))
side_c = float(input("Enter Side C: "))
side_d = float(input("Enter Side D: "))

def DefineFigureType(side_a, side_b, side_c, side_d):
    if side_a**2 + side_b**2 == side_c**2 + side_d**2 and side_a == side_c and side_b == side_d:
        return True
    else:
        return False


def IsSquare(side_a, side_b, side_c, side_d):
    if side_a == side_b == side_c == side_d:
        return True
    else:
        return False

def CalcRectangleArea(side_a, side_b):
        return side_a * side_b


def UserOutput():
    if IsSquare(side_a, side_b, side_c, side_d):
        print("Це квадрат")
    elif DefineFigureType(side_a, side_b, side_c, side_d):
        print("Це прямокутник")
        print("Площа дорівнює", CalcRectangleArea(side_a, side_b))
    else:
        print("Це не квадрат і не прямокутник")

UserOutput()



"""
2. Дано списки names и domains (створити самостійно).Написати функцію для генерування e-mail 
в форматі:
прізвище.число_від_100_до_999@рандомна_стрічка_букв_довжиною_від_5_до_7_символів.домен
прізвище і домен брати випадковим чином з заданих списків переданних в функцію в вигляді параметрів.
трічку і число генерувати випадковим чином.

Приклад використання:

names = ["king", "miller", "kean"]

domains = ["net", "com", "ua"]

e_mail = create_email(domains, names)

print(e_mail)>>>miller.249@sgdyyur.com
"""
import random
import string


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]

def CreateEmail(domains, names):
    email_name = names.pop()
    email_id = random.randint(100, 999)
    body_len = random.randint(5, 7)
    random_body = ''.join(random.choices(string.ascii_lowercase, k=body_len))
    email_domain = domains.pop()
    email = (f'{email_name}{email_id}@{random_body}.{email_domain}')
    return email

e_mail = CreateEmail(domains, names)

print(e_mail)
