def hello(func):
    def get_name():
        name = input('Введите имя: ')
        return func() + name
    return get_name

@hello
def result():
    return 'Привет, '

print(result())


