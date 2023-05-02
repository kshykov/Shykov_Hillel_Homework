from abc import ABC, abstractmethod

class PrintedProduct(ABC):
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    @abstractmethod
    def print_details():
        pass

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, new_author):
        self.__author = new_author

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price


class ArtPrint(PrintedProduct):

    def __init__(self, title, author, price, paper):
        super().__init__(title, author, price)
        self.paper = paper

    def print_details(self):
        print(f'You can buy Art Print "{self.title}" by {self.author} on {self.paper} with only {self.price}')
        
class CanvasPrint(PrintedProduct):
    def __init__(self, title, author, price, frame):
        super().__init__(title, author, price)
        self.frame = frame

    def print_details(self):
        print(f'You can buy Canvas Print "{self.title}" by {self.author} with {self.frame} frame and with only {self.price}')


art_print_1 = ArtPrint("Clouds at the night", "Cho Lee", 99.99, "paper")
canvas_1_ = CanvasPrint("Burger menu", "David-D", 9999, "metal")


art_print_1.print_details()
canvas_1_.print_details()
print(art_print_1.author)
print(canvas_1_.title)