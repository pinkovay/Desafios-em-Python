from random import randint
from operator import itemgetter
jogador = {'Jogador 1': randint(1, 6),
           'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6),
           'Jogador 4': randint(1, 6)}
ranking = dict()
print('_' * 40)
for k, v in jogador.items():
    print(f'{f"{k} tirou: {v}":^40}')
print('_' * 40)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

print(f'{"RANKING":^40}')
for k, v in ranking:
    print(f'{f"{k}, com o número {v}":^40}')