geral = list()
pessoa = dict()
mulheres = list()
idades = list()
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    pessoa['nome'] = nome
    sexo = input('Sexo : ').upper()
    while sexo not in 'MF':
        sexo = input('Digite apenas M ou F: ').upper()[0]
    if sexo in 'F':
        mulheres.append(nome)
        pessoa['sexo'] = sexo
    else:
        pessoa['sexo'] = sexo

    idade = int(input('Idade: '))
    pessoa['idade'] = idade
    idades.append(idade)
    geral.append(pessoa.copy())
    desejo = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while desejo not in 'SN':
        desejo = input('Digite algo válido: ')
    if desejo in 'N':
        print('_' * 40)
        break
    elif desejo in 'S':
        print('_' * 40)
print(f'A) Ao todo temos: {len(geral)} pessoas cadastradas')
print(f'B) A média de idade é {sum(idades) / len(geral):5.2f} anos')
media = sum(idades) / len(geral)
print(f'C) As mulheres cadastradas foram: {mulheres}')
print('D) Lista de pessoas que estão acima da média de idade: ')
for p in geral:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('_' * 40)
