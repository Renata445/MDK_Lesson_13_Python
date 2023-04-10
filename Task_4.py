a = input('Введите предложение, которое хотите расшифровать: ')
def cesar(str, key):
    decrypted = ""
    for i in str:
        if i.isupper():
            index = ord(i) - ord('А')
            og_pos = (index - key) % 32 + ord('А')
            og = chr(og_pos)
            decrypted += og
        elif i.islower():
            index = ord(i) - ord('а')
            og_pos = (index - key) % 32 + ord('а')
            og = chr(og_pos)
            decrypted += og
        else:
            decrypted += i
    return decrypted

print(cesar(a, 3))