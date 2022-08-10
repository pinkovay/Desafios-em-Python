print('Conversor de BRL para DOL e EURO, cotação de 5.53')
real=float(input('Quantos reais você tem em sua carteira? '))
dl = real / 5.53
eur = real / 6.33
print(f'Você pode transformar R${real} em {dl} doláres')
print(f'Você pode transformar R${real} em {eur} euros')
