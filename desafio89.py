alunos = list()
temporaria = list()
aluno = 1
while True:
    temporaria.append(str(input('Aluno: ')))
    temporaria.append(float(input('Nota: ')))
    temporaria.append(float(input('Nota: ')))
    aluno += 1
    alunos.append(temporaria[:])
    temporaria.clear()
    confirm = str(input(f'Deseja adicionar um {aluno}º aluno? [S/N] '))
    if confirm in 'Ss':
        print('-' * 20)
    elif confirm in 'Nn':
        break
print('_' * 40)
print(f'{"NÚMERO":^5} {"ALUNO":^20} {"MÉDIA":>10}')
for i, al in enumerate(alunos):
    media = (al[1] + al[2]) / 2
    print(f'{i:^5} {al[0]:^20} {media:>10}')
print('_' * 40)
while True:
    nts = int(input('Mostrar notas de qual aluno?    [999 INTERROMPE] '))
    if nts == 999:
        break
    if nts < 0 or nts > 2:
        print('Digite um valor válido')
    else:
        print('_' *40)
        print(f'As notas de {alunos[nts][0].capitalize()} foram: {alunos[nts][1]:.2f} e {alunos[nts][2]:.2f} ')
        print('_' * 40)
print('_' * 40)
print('Programa encerrado')