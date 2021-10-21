class Engines():
    """Класс машины"""
    tyres = 4
    cabine = True
    def __init__(self, name="Какой-то транспорт"):
        self.name = name

    def view_engines(self):
        print("У всех машин есть колеса, шт...", self.tyres)
        print("Есть или нет кабина...", self.cabine)
        print(self.__class__.__name__)
        print(self.__class__.__dict__)


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

    def inspect(self):
        print(self.__class__.__name__)
        print(self.__dict__)
        print(self.tyres)


track1 = Tractor()
track1.sound()
track1.view_engines()
print("+++++++++++++++++++++++ +++++++++++++++++++++++++")
track1.tyres = 5
track1.inspect()
print(track1.tyres)

class Parent():
    class_var1 = 11
    class_var2 = 21
    class_var3 = 31

    def __init__(self):
        self.var_1 = 12
        self._var_2 = 22
        self.__var_3 = 32

    def parent_method(self):
        print(self.class_var1)
        print(self.class_var2)
        print(self.class_var3)
        print(self.var_1)
        print(self._var_2)
       # print(self.__var_3)

class Child(Parent):
    def child_method(self):
        print(self.class_var1)
        print(self.class_var2)
        print(self.class_var3)
        print(self.var_1)
        print(self._var_2)
       # print(self.__var_3)

obj = Child()
obj.parent_method()
obj.child_method()
