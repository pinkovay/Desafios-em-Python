import datetime
ano = int(input('Ano de nascimento: '))
anoatual = datetime.date.today().year
print(f'Quem nasceu em {ano}, tem/fará {anoatual-ano} anos em {anoatual}')
if anoatual-ano <= 17:
    alis1 = 18 - (anoatual-ano)
    print(f'Seu alistamento será em {anoatual + alis1}')
elif anoatual-ano == 18:
    print('Seu alistamento é este ano, boa sorte!!')
else:
    alis2 = (anoatual-ano) - 18
    print(f'Seu alistamento foi em {anoatual - alis2}')
