
def my_func():
    #global x
    x = 'll'
    print(f'эта переменная x внутри функции - {x}')
    print(locals())


my_func()
#print(globals())

def func_1():

    def func_2():
        print('Внутри func_2 x равен:', x)

    print('Внутри func_2 x равен:', x)
    func_2()

x = 5
func_1()
print(x)



