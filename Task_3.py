def honest(number):
    return number % 2 == 0

lst = [i for i in range(0, 21)]
print(*filter(honest, lst))