import datetime
soma = 0
for c in range(1, 8):
    nascimento = int(input(f'Ano de nascimento da {c}° pessoa: '))
    anoatual = datetime.date.today().year
    idade = anoatual - nascimento
    if idade >= 18:
        soma += 1
if soma == 0:
    print('Nenhuma dessas pessoas é de maior ainda.')
elif 1 < soma <= 3:
    print(f'Apenas {soma} das 7 pessoas já são adultas.')
elif 4 < soma <= 6:
    print(f'{soma} dessas pessoas já atingiram a maioridade')
elif soma == 7:
    print('Todos já se tornaram de maior.')