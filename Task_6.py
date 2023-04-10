# a)
def alphabet():
    for i in range(65, 91):
        print(f'Порядковый номер буквы {chr(i)}: {ord(chr(i)) - ord(chr(65)) + 1}')

alphabet()

# б)
def alphabet2():
    letters = []
    for i in range(65, 91):
        letters.append(chr(i))
    numbers = []
    for i in range(65, 91):
        numbers.append(ord(chr(i)) - ord(chr(65)) + 1)
    Mydict = {numbers[i]: letters[i] for i in range(0, len(numbers), 1)}
    print(Mydict)

alphabet2()

