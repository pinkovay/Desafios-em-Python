ve = float(input('Qual a velocidade do veículo? Km/h:'))
if ve < 80:
    print('Está dentro do limite da via registrada!!')
else:
    mul = (ve - 80) * 7.0
    acima = ve - 80
    print(f'Está {acima}Km/h acima do limite, a multa deverá ser de: R${mul}')
    
