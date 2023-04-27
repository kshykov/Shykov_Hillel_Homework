class Dog:
    def __init__(self, name, limbs, tail, color, voice):
        self.name = name
        self.limbs = 4
        self.tail = ["long", "short", "middle"]
        self.color = ["solid", "tortoise", "mixed"]
        self.voice = voice

    @staticmethod
    def dog_vs_cats():
        print("Dogs are better then cats")


class Company:
    def __init__(self, title, total_staff, activity):
        self.title = title
        self.total_staff = total_staff
        self.activity = activity

    @classmethod
    def company_type(cls, total_staff):
        if 1 <= total_staff <= 15:
            print("Startup")
        elif 16 <= total_staff <= 50:
            print("Small company")
        elif 51 <= total_staff <= 99:
            print("Middle company")
        elif total_staff >= 100:
            print("Big company")
        else:
            print("You need to hire staff")


my_dog = Dog("Monro", 4, "middle", "solid", "gav-gav")

my_dog.dog_vs_cats()

middle_company_1 = Company("First middle company", 99 , "Retail")

Company.company_type(middle_company_1.total_staff)