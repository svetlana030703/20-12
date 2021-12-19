nom = list(map(int, input().split(", ")))

def sum(nom):
    ol = 0
    for x in nom:
        ol += x
    return ol
print(sum(nom))
