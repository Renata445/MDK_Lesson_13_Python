s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']

def transformation(names):
    name = ''.join(filter(str.isalpha, names))
    name = name.capitalize()
    return name




transformations = list(map(transformation, s))
print(transformations)

