import emoji
print(emoji.emojize(':red_car: Programa usado para calcular valor a ser pago para aluguel de carro :red_car:', use_aliases=True))
dia = float(input('Quanto é cobrado por dia de uso?:'))
dia2 = float(input('Por quantos dias foi alugado?:'))
km = float(input('E por quilômetros rodado, quanto é cobrado? :'))
km2 = float(input('Ok, e por último, quantos quilômetros foram rodados?:'))
vd = dia * dia2
vkm = km * km2
vdt= vd + vkm
print(emoji.emojize(f':red_car: O valor a ser pago, é de: R${vdt} :red_car:', use_aliases=True))
