total = 0
n = int(input('Diga um número inteiro: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {n} foi divisivvel {total} vezes')
if total == 2:
    print(f'{n} é um número primo')
else:
    print(f'{n} Não é um número primo')

