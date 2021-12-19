text = str(input())
n = sorted(text.split('-'))
w = text.split()
e=""
for r in sorted(w):
    e=e+" " +r
print(e)
#join объединение списка строк с помощью определенного указателя
