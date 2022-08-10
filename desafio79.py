sequencia = list()
while True:
    n = float(input('Digite um valor: '))
    if not n in sequencia:
        sequencia.append(n)
    else:
        print('Número repetido, não será adicionado. ')
    confi = input('Deseja adicionar mais um número? [S/N]: ').upper()
    if confi == 'S':
        print('_' * 20)
    else:
        sequencia.sort()
        print(sequencia)
        break