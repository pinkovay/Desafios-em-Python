temporaria = list()
principal = list()
pesados = list()
leves = list()
maior = menor = 0
c = 0
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    con = str(input('Deseja continuar? [S/N]: '))
    if con in 'Nn':
        break
print('_' * 30)
print(f'Você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}Kgs. Peso de: ', end='')
for p in principal:
    if p[1] == maior:
        if c == 0:
            print(f'{p[0]}', end='')
            c += 1
        else:
            print(f', {p[0]}')
print('')
print(f'O menor peso foi de {menor}Kgs. Peso de: ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')










