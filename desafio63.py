print('=' * 22)
print('Sequência de Fibonacci')
print('=' * 22)
quant = int(input('Quantos termos da sequencia deseja ver? '))
t1 = 0
t2 = 1
cont = 3
print('=' * 22)
print(f'{t1} ➢ {t2}', end='')
while cont <= quant:
    t3 = t1 + t2
    print(f'➢ {t3}', end='')
    cont += 1
    t1 = t2
    t2 = t3
print('➢ fim')

