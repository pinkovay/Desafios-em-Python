p1 = int(input('Primeiro número da PA: '))
razao = int(input('Qual sua razão? '))
mais = int(input('Deseja ir até qual termo primeiramente? '))
termo = p1
cont = 1
total = 0

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ➫ ', end='')
        cont += 1
        termo = termo + razao
    print('PAUSA')
    mais = int(input('Quantos termos você deseja ver a mais? '))
print(f'PA finalizada com {total} termos.')
