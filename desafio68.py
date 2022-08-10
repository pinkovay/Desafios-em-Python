import random
contador = vito = 0
print('-' * 40)
print('VAMOS JOGAR PAR OU IMPAR')
print('-' * 40)
while True:
    jogador = int(input('Escolha um número: '))
    jogador2 = str(input('PAR ou IMPAR? ')).upper().strip()
    if jogador2 == 'PAR':
        contador += 1
        computador = random.randint(1,10)
        print(f'Computador: {computador}')
        soma = computador + jogador
        if soma // 2 == 0:
            vito += 1
            print('-' * 40)
            print(f'Parabéns, você venceu!!, até agora você ganhou {vito}', 'vez' if contador == 1 else 'vezes')
            print('-' * 40)
        else:
            if contador == 1:
                print('-' * 40)
                print(f'Eu ganhei hahaha, você jogou apenas {contador} vez ')
                print('-' * 40)
                break
            else:
                print('-' * 40)
                print(f'Eu ganhei hahaha, você jogou {contador} vezes, e ganhou {vito} vezes')
                print('-' * 40)
                break
    else:
        contador += 1
        computador = random.randint(1, 10)
        print(f'Computador: {computador}')
        soma = computador + jogador
        if soma // 2 != 0:
            vito += 1
            print('-' * 40)
            print(f'Parabéns, você venceu!!, até agora você ganhou {vito}', 'vez' if contador == 1 else 'vezes')
            print('-' * 40)
        else:
            if contador == 1:
                print('-' * 40)
                print(f'Eu ganhei hahaha, você jogou apenas {contador} vez ')
                print('-' * 40)
                break
            else:
                print('-' * 40)
                print(f'Eu ganhei hahaha, você jogou {contador} vezes, e ganhou {vito} partidas.')
                print('-' * 40)
                break
print('Reinicie o jogo')
