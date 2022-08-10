matriz = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
par = n = m_s = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            n += matriz[l][c]
        if l == 1:
            if matriz[l][c] > m_s:
                m_s = matriz[l][c]
print('_' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('_' * 30)
print(f'A soma de todos os números pares é: {par}')
print(f'A soma de todos os números da terceira coluna é: {n}')
print(f'O maior número da segunda linha é: {m_s}')





