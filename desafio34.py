salario = float(input('Qual o salário do funcionário? R$'))
if salario <= 1250.00:
    aum = salario / 100 * 15
    aum1 = salario + aum
    print(F'Com um aumento de 15%, o salário indicado, passaria a ser de R${aum1}')
else:
    aum2 = salario / 100 * 10
    aum3 = salario + aum2
    print(f'Com um aumento de 10%, o salário indicado, passaria a ser de R${aum3}')
