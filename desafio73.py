time = ("Flamengo", "Palmeiras", "Atlético Mineiro", "Grêmio", "Atlético Paranaense", "Santos", "São Paulo", "Internacional", "Fluminense", "Corinthians", "Fortaleza", "Bahia", "Ceará", "Cruzeiro", "América Mineiro", "Atlético Goianense", "Chapecoense", "Botafogo", "Vasco da Gama", "Red Bull Bragantino")
print('Os cinco primeiros colocados da tabela do brasileirão de 2022 são:')

print('=' * 20)
for c in range(0, 5):
    print(time[c])

#print('Os quatro últimos são:')
#for u in range(-4, 0):
    #print(time[u])

print('=' * 20)
print(f'Os quatro últimos times são:: {time[-4:]}')
print('=' * 20)
print(f'Os times em ordem alfabética ficam: {sorted(time)}')

print('=' * 20)
print(f'A chapecoense está em:', (time.index('Chapecoense')+1))
print('=' * 20)

