n = list(map(int, input().split(", ")))
def f(n):
    m = []
    for i in n:
        if i % 2 == 0:
            m.append(i)
    return m
print(f(n))
