p1 = int(input('Primeiro número da PA: '))
razao = int(input('Qual sua razão? '))
termo1 = int(input('Deseja que façamos até qual termo? '))
termo = p1
cont = 1
while cont <= termo1:
    print(f'{termo} ➫ ', end='')
    cont += 1
    termo = termo + razao
print('FIM')


