dis = float(input('Qual a distância da viagem? Km'))
if dis <= 200:
    valor = dis * 0.50
    print(f'Com a distância de {dis}Km, o valor da passagem será: R${valor}')
else:
    valor2 = dis * 0.45
    print(f'Com a distância de {dis}Km, o valor da passagem será: R${valor2}')
print('Tenha uma ótima viagem!!')
