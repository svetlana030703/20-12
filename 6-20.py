print('Введите число')
n = int(input())
print('Введите диапазон')
a, b = map( int, input().split())

def f(n):
    vh = "Входит"
    nv = "Не входит"
    if n - a >= 0 and b - n >= 0:
        return vh
    else: nv
print( f(n))
