'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
import random
computador = random.randint(1,10)
tentativas = 0
jogador = int(input('Em qual número você acha que pensei? (1 a 10) '))
if computador != jogador:
    while computador != jogador:
        if computador != jogador:
            jogador = int(input(f'Você errou, tente novamente:'))
            tentativas += 1
            if computador == jogador:
                print(f'Parabéns, você acertou!, eu pensei no {computador} mesmo, foram necessárias {tentativas} tentativas dessa vez.')
else:
    print(f'UAU, você acertou de primeira!!, eu pensei no {computador} mesmo')



