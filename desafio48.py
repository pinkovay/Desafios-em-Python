s = 0
cont = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        print(c)
        s += c
        cont += 1
print(f'A soma de todos os {cont} números impares, múltiplos de 3, entre 1 e 500, é:{s}')
