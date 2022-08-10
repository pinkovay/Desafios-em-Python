import random
print('==' * 10, 'PEDRA, PAPEL OU TESOURA', '==' * 10)
itens = ('Pedra', 'Papel', 'Tesoura')
comput = random.randint(0, 2)
jogador = int(input('Suas opções:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\nQual sua escolha? '))
print('==' * 10)
print(f'Computador jogou {itens[comput]}')
print(f'Jogador jogou {itens[jogador]}')
print('==' * 10)
if comput == 0: #pedra
    if jogador == 1:
        print('VOCÊ GANHOU, PARABÉNS!!')
    elif jogador == 2:
        print('EU GANHEI!!')
    elif jogador == comput:
        print('NÓS EMPATAMOS!!')
elif comput == 1: #papel
    if jogador == 2:
        print('VOCÊ GANHOU, PARABÉNS!!')
    elif jogador == 0:
        print('EU GANHEI!!')
    elif jogador == comput:
        print('NÓS EMPATAMOS!!')
elif comput == 2: #tesoura
    if jogador == 0:
        print('VOCÊ GANHOU, PARABÉNS!!')
    elif jogador == 1:
        print('EU GANHEI!!')
    elif jogador == comput:
        print('NÓS EMPATAMOS!!')
else:
    print('DIGITE ALGO VÁLIDO')
print('==' * 10)
