import datetime
ano = datetime.date.today().year
print('A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade')
nascimento = int(input('Ano de nascimento: '))
idade = ano - nascimento
if idade == 1:
    print(f'O mini atleta tem {idade} ano')
if idade > 1:
    print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif 14 < idade <= 19:
    print('Classificação: JÚNIOR')
elif 19 < idade <= 25:
    print('Classificação: SÊNIOR')
elif idade >= 26:
    print('Classificação: MASTER')
else:
    print('Digite algo válido.')
