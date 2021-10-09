def print_all_params(*args, **kwargs):
    """This function printing all params!"""
    print("Неименованные параметры:")
    for i, elem in enumerate(args):
        print("Позиция параметра:", i, "Значение:", elem)
    print("Именованные параметры:")
    for i, elem in kwargs.items():
        print("Название параметра:", i, "Значение:", elem)

print_all_params(16, 2, "Взвешивание", ryba="Сельдь", edinica="кг")
