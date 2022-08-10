homem = mulher = mulher21menos = 0
usuario = 0
maior18 = menor18 = 0
while True:
    nome = input('Diga o nome do usuário: ').strip().capitalize()
    usuario +=1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'Qual o sexo de {nome}? [M/F]')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    elif sexo == 'F':
        mulher += 1
    idade = int(input(f'Quantos anos {nome} tem? '))
    if idade >= 18:
        maior18 += 1
    elif idade < 21 and sexo == 'F':
        mulher21menos += 1
    else:
        menor18 += 1
    continuacao = ' '
    while continuacao not in 'SN':
        continuacao = str(input(f'Deseja registrar um {usuario + 1}º usuário? [S/N]')).strip().upper()[0]
    if continuacao == 'N':
        break
print(f'Você registrou {usuario} usuários(as)')
print(f'{maior18} deles são de maior')
print(f'Foram registrados {mulher} mulheres e {homem} homens')
print(f'Dessas mulheres, {mulher21menos} tem menos de 21 anos')

