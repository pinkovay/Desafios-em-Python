jogador = dict()
gols = list()
total = 0
partida = 0
jogador['Nome'] = str(input('Nome do jogador: '))
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, jogador['Partidas']):
    gols.append(int(input(f'Quantos gols {jogador["Nome"]} fez na {c+1}º partida: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('_' * 80)
print(f'                   {jogador["Nome"]} jogou {len(jogador["gols"])} partidas')
c = 1
for i, v in enumerate(jogador['gols']):
    print(f'                 =>Na partida {i + 1}, fez: {v} gols ')

print('_' * 80)
print(F'             {jogador["Nome"]} fez {jogador["total"]} gols ao total em {jogador["Partidas"]} partidas')
print('_' * 80)
for k, v in jogador.items():
    print(f'{f"O campo {k} tem o valor: {v}":^80}')
