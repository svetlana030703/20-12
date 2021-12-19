t = 'prostoe '
f = 'ne prostoe '
n= int(input())

def f(n):
    if n == 1:
        return f
    elif n == 2:
        return t
    elif n > 2:
        if n % 2 == 0:
            return f
        else:
            r = 0
            for i in range (1, n+1, 2):
                if n % i == 0:
                    r += 1
                    if r > 2:
                        return f
                if r == 2:
                    return t

print(f(n))
