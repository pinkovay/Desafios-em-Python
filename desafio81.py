lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    cn = str(input('Deseja continuar digitando? [S/N]'))
    if cn in 'Nn':
        print('_' * 30)
        print(f'Você digitou {len(lista)} números')
        lista.sort(reverse=True)
        print('Sua sequencia de trás para frente fica: ',lista)
        if lista.count(5):
            print('Você digitou', lista.count(5), 'vezes o número 5')
        break
