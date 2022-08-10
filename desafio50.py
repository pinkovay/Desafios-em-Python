S = 0
for c in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        S += n
if S == 0:
    print('Não há o que somar, ou só foram digitados números ímpares.')
else:
    print(f'A soma de todos os números pares digitado, é: {S}')

