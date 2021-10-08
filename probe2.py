def my_func():
    """Do X and return a list."""
    pass

print(my_func.__doc__)


jj = [4, 5, 7, 1, 2, 3, 12]
y = 14
flag1 = 0
flag2 = 0
for elem in jj:
    razn = elem - y
    for i in jj:
        if i == razn:
            flag1 = i
            flag2 = elem
print(flag1, flag2)



