import random

a = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 '
b = int(input('сколько паролей: '))
c = int(input('длина паролей: '))
for n in range(b):
    passw =''
    for i in range(c):
        passw += random.choice(a)
    print(passw)
