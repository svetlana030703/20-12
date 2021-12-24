def f(n ,m):
    dict_ = {}

    if len(n) == len(m):
        for n,m in zip(names,ages):
            dict_[n] = m
        return(dict_)
    else:
        print('Списки имеют разную длину')

names = []
ages = []
n = int(input())
m = int(input())

for i in range(n):
    names.append(input())

for i in range(m):
    ages.append(input())

print(f(names,ages))