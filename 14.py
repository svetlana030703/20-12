def aaaa(k=''):
    k=k.lower()
    j=""
    alf="абвгдежзиклмнопрстуфхцчшщыэюя"
    for i in k:
        if str.isalpha(i): #возвращение как true false
            if i in alf:
                if i not in j:
                    j+=i
    if len(j)>=len(alf):
        print("панограмма русского языка")
    else: print("не панограмма русского языка")
aaaa()