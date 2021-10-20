class MyCars:
    def __init__(self):
        self.color = 'white'
        self.power = 124
        self.speed = 0

    def __del__(self):
        print("Перед тем как попасть на свалку была машина цвета: ", self.color)

    def __str__(self):
        return "Печатаем состояние объекта:" + self.color + ', ' + str(self.power) + ', ' + str(self.speed)

    def __add__(self, other):
        sum_car_power = []
        if isinstance(other, MyCars):
            sum_car_power.append(self.power)
            sum_car_power.append(other.power)
        elif isinstance(other, list):
            sum_car_power.append(self.power)
            sum_car_power.append(*other)

        return sum_car_power

    def __iadd__(self, other):
        self.power = self.power + other.power
        return self.power

class MyFunctions:
    def __init__(self, dobavka=10):
        self.dobavka = dobavka

    def __call__(self, *args, **kwargs):
        for item in args:
            print("Вывод функции-объекта класса:", item+self.dobavka)
        for item in kwargs.values():
            print("Вывод функции-объекта класса:", int(item)+self.dobavka)



first_car = MyCars()
second_car = first_car
print(second_car.color)

second_car.color = 'blue'
print(first_car.color)

second_car.height = 150
print(second_car is first_car)
attrib = 'height2'
print("Есть такой атрибут" if hasattr(first_car, attrib) else setattr(first_car, attrib, 55))

print(first_car)
print(getattr(first_car, attrib))

third_car = MyCars()
third_car.power = 320
# print(first_car+[16])

first_car += third_car
print(first_car)


func_1 = MyFunctions(dobavka=1000)
func_1(a=3,b=8)
func_1(a=1,b=5)
func_1(12,18)