def f():
    a = 'hohoho'
    b = 73
    c = "kuku"
    x = 674
#название функции и .__code__.co_nlocals определяет кол-во переменных
print(f.__code__.co_nlocals)
