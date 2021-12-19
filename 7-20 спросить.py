n = input()

def f(n):      
    u = sum(1 for i in n if i.isupper())
    l = sum(1 for i in n if i.islower())
    return u, l

print(f(n))

#почему он считает пробелы? так должно быть?
