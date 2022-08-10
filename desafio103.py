def Player(nome="<Desconhecido>", gol=0):
    print(f'O jogador {nome} fez {gol} gol(s).')


nome = str(input('Nome do jogador: ')).strip().capitalize()
g = str(input('Quantidade de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    Player(gol=g)
else:
    Player(nome, g)


