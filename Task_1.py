oper = input('Введите оперцию: ')
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
def calculate(operation, num_1, num_2):
    if operation == '*':
        print(eval(f'{num_1}{operation}{num_2}'))
    elif operation == '+':
        print(eval(f'{num_1}{operation}{num_2}'))
    elif operation == '-':
        print(eval(f'{num_1}{operation}{num_2}'))
    elif operation == '/':
        if num_2 != 0:
            print(eval(f'{num_1}{operation}{num_2}'))
        else:
            print('Делить на ноль нельзя!')

calculate(oper, number_1, number_2)