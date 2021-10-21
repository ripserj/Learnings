class Engines():
    """Класс машины"""
    tyes = 4
    cabine = True
    def __init__(self, name="Какой-то транспорт"):
        self.name = name

    def view_engines(self):
        print("У всех машин есть колеса, шт...", self.tyes)
        print("Есть или нет кабина...", self.cabine)
        print(self.__class__.__name__)
        print(self.__dict__)


class Lorries(Engines):
    def __init__(self):
        self.color = "Красный"

    def sound(self):
        print("Врррр!!!")


class Cars(Engines):
    def __init__(self):
        self.color = "Красный"

    def sound(self):
        print("Хынь-хынь!!!")


class Tractor(Engines):
    def __init__(self):
        self.color = "Красный"

    def sound(self):
        print("Тр-тр-тр!!!")


track1 = Tractor()
track1.sound()
track1.view_engines()