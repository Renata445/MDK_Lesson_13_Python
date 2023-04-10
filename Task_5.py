def countdown():
    lst = [i for i in range(0, 11)]
    a = list(reversed(lst))
    for i in a:
        if i == 0:
            a.append('Пуск!')
    return a



print(countdown())