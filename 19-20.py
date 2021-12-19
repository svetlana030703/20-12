n = int(input())

def f(n):
        def g(x):
                nonlocal n
                #переменная осьается неизменной, после выхода из функции
                n += 1
                return n+x
        return g
m = f(n)
print(m(n))
