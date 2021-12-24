def f(n ,m):
    dict_ = {}

    if len(n) == len(m):
        for n,m in zip(nam,ag):
            dict_[n] = m
        return(dict_)
    else:
        print('Списки имеют разную длину')

nam = []
ag = []
n = int(input())
m = int(input())

for i in range(n):
    nam.append(input())

for i in range(m):
    ag.append(input())

print(f(nam,ag))
