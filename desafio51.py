
print('==' * 40)
p1 = int(input('Diga o primeiro termo da PA: '))
r = int(input('Agora sua razão: '))
d = p1 + (11 - 1) * r
print('==' * 40)
for c in range(p1, d, r):
    print(f'{c}', end=' ➪ ')
print('ACABOU')