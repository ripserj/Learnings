class MyCars:
    def __init__(self):
        self.color = 'white'
        self.power = 124
        self.speed = 0


first_car = MyCars()
second_car = first_car
print(second_car.color)

second_car.color = 'blue'
print(first_car.color)

second_car.height = 150
print(second_car is first_car)
attrib = 'height2'
print("Есть такой атрибут" if hasattr(first_car, attrib) else setattr(first_car, attrib, 55))

print(getattr(first_car, attrib))
