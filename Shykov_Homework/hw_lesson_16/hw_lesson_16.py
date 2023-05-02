from abc import ABC, abstractmethod

class Tram(ABC):
    def __init__(self, route_number, capacity):
        self.route_number = route_number
        self.capacity = capacity

    @abstractmethod
    def drift(self):
        pass


class KharkivTram(Tram):
    def __init__(self, route_number, capacity, year_of_manufacture):
        super().__init__(route_number, capacity)
        self.year_of_manufacture = year_of_manufacture

    def drift(self):
        print(f"Харківський трамвай на марщруті {self.route_number} виконує трамвайний дріфт")



class NewTram(KharkivTram):
    def __init__(self, route_number, capacity, year_of_manufacture):
        super().__init__(route_number, capacity, year_of_manufacture)

    def drift(self):
        print(f"Новий Харківський трамвай {self.year_of_manufacture} року виробництва на марщруті {self.route_number} "
              f" виконує трамвайний дріфт")



class OldTram(KharkivTram):
    def __init__(self, route_number, capacity, year_of_manufacture):
        super().__init__(route_number, capacity, year_of_manufacture)

    def drift(self):
        print(f"Старий Харківський трамвай {self.year_of_manufacture} року виробництва на марщруті {self.route_number} "
              f" виконує трамвайний дріфт")


new_tram = NewTram(16, 100, 2010)
old_tram = OldTram(27, 100, 1970)

new_tram.drift()
old_tram.drift()