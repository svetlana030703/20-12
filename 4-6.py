import math 

a = [float (i) for i in input().split()]

def f(n):
    for i in a:
        if i > 0:
            print (math.log1p(i))
        else:
            print ("None")

f(a)

