jogador = dict()
geral = list()
gols = list()
while 1:
    nome = str(input('Nome do jogador: ')).strip().capitalize()
    jogador['nome'] = nome
    partida = int(input(f'Quantas partidas {nome} jogou: '))
    for p in range(0, partida):
        gols.append(int(input(f'Quantos gols na {p+1}º partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    geral.append(jogador.copy())
    print()
    conf = str(input('Deseja adicionar mais alguém? [S/N]: ')).strip().upper() [0]
    while conf not in 'SN':
        conf = str(input('Digite apenas [S/N]: ')).strip().upper() [0]
    if conf in 'S':
        print('_' * 40)
    elif conf in 'N':
        print('_' * 40)
        break
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(geral):
    print(f'\033[33m{k:<4}\033[m', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('_' * 40)
while 1:
    info = int(input('Deseja ver a informação de qual jogador? [999 PARA PARAR]: '))
    if info == 999:
        print('_' * 40)
        break
    if info > len(geral) or info < 0:
        print('Digite algo válido.')
    else:
        for i, g in enumerate(geral[info]['gols']):
            print(f'     no jogo {i + 1} fez {g} gols')
    print('_' * 40)







