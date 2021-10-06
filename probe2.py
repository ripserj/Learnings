a = [int(x) for x in input().split(',')]
y = int(input())
flag1 = 0
flag2 = 0
for elem in a:
    razn = elem - y
    for i in a: 
        if i == razn:
            flag1 = i
            flag2 = elem
print(flag1, flag2) 