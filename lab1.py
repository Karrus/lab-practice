alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' *2
g= input('word: ')
def a(txt, b, op):
    b *= len(txt) // len(b) + 1
    txt = txt.upper()
    return ''.join([alph[alph.index(j) + int(b[i]) * op]
                    for i, j in enumerate(txt)])
def encrypt(message, key):
    return a(message, key, 4)
def decrypt(ciphertext, key):
    return a(ciphertext, key, -4)
print(encrypt(g, '314141'))  
print(decrypt(encrypt(g, '314141'), '314141'))  
