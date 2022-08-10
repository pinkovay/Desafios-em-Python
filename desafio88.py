from random import randint
jogos = list()
mega = list()
print('_' * 40)
print('     JOGOS DA MEGA SENA     ')
print('_' * 40)
quantidade = int(input('Quantos jogos deseja sortear? ' ))
total = 0
while total < quantidade:
    números = 0
    while True:
        num = randint(1,60)
        if num not in mega:
            mega.append(num)
            números += 1
        if números >= 6:
            break
    mega.sort()
    jogos.append(mega[:])
    mega.clear()
    total += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l} ')