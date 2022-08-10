peso = float(input('Qual é seu peso? Kg'))
altura = float(input('E sua altura? '))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO do peso normal, se alimente direito, e se for preciso, vá ao médico. ')
elif 18.5 <= imc < 25:
    print('Parabéns, você está em seu peso IDEAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO, uma alimentação um pouco melhor, e isso se resolve rapidamente.')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE, consulte um médico.')
elif imc > 40:
    print('Você está com OBESIDADE MÓRBIDA, consulte um médico urgentemente!!')
    