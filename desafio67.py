while True:
    print('-' * 40)
    tabuada = float(input('Deseja ver a tabuada de qual número? '))
    print('-' * 40)
    if tabuada <= 0:
        break
    for s in range(1, 11):
        print(f'{tabuada} x {s} = ', tabuada * s)
print('Programa encerrado, só utilizamos números acima de 1')
