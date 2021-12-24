import math 

a = [float (i) for i in input().split()]

def calc(a_list):
    for numbers in a:
        if numbers > 0:
            print (math.log1p(numbers))
        else:
            print ("None")


calc(a)

