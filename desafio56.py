n = 0
maioridade = 0
mulher = 0
nomevelho = 0
for c in range(1,5):
    print('--' * 10, f'{c}ª PESSOA', '--' *10)
    nome = str(input('Nome: ')).capitalize().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if c == 1 and sexo == 'M':
        maioridade = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if idade >= 0:
        n += idade
    if sexo == 'M':
        homem = nome, idade
    if sexo == 'F' and idade < 20:
        mulher += 1
media = n // 4
print(f'A média de idade dessas pessoas é de: {media}')
print(f'O homem mais velho tem {maioridade} anos, e se chama {nomevelho}')
print(f'{mulher} Mulher(es) tem menos de 20 anos')






'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''


