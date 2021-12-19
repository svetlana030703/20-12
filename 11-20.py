n = int(input())
a = "совершенное"
b = "не совершенное"
def f(n):
    m = 0
    for i in range(1, n):
        if n % i == 0:
            m += i
    if m == n:
        return a
    else: return b
print(f(n))
