import datetime
anoatual = datetime.date.today().year
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
idade = int(input('Ano de nascimento: '))
idade = anoatual - idade
pessoa['Idade'] = idade
ctps = int(input('Número da carteira de trabalho: [0 NÃO TEM]: '))
if ctps != 0:
    pessoa['Carteira de trabalho'] = ctps
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Aposenadoria'] = (pessoa['Ano de contratação'] + 35) - anoatual + pessoa['Idade']
print('_' * 40)
for k, v in pessoa.items():
    print(f'{f"-{k} tem o valor de: {v}":>20}')
