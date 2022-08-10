notas = dict()
n = list()


def Notas(notas):
    media = 0
    global maior, menor
    for c in range(0, len(notas['notas'])):
        if c == 0:
            maior = notas['notas'][c]
            menor = notas['notas'][c]
        if c > 0 and notas['notas'][c] >= maior:
            maior = notas['notas'][c]
        if c > 0 and notas['notas'][c] <= menor:
            menor = notas['notas'][c]
        media += notas['notas'][c]
    media = media / len(notas["notas"])
    print(f'\033[31mA maior nota foi: {maior}\n A menor nota foi: {menor}\n A média da turma é {media:.2f}')
    if media >= 5:
        situ = 'Aprovada'
    else:
        situ = 'Reprovada'
    print(f'A turma foi: {situ}')
    print(f'Foram apresentadas {len(notas["notas"])} notas')


a = 1
while 1:
    nota = float(input(f'{a}º Nota: '))
    n.append(nota)
    conf = str(input('Deseja adicionar mais alguma nota? ')).strip()[0]
    a += 1
    if conf in 'Nn':
        notas['notas'] = n[:]
        break
Notas(notas)
