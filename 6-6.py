def f(numbers):
    numbers.sort()
    return(numbers)

print(f(numbers = [int(number) for number in input().split(', ')]))
