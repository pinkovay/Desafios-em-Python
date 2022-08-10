s = q = 0
while True:
    n = int(input('Digite um número [999 pra parar]: '))
    if n == 999:
        break
    s += n
    q += 1
print(f'A soma de todos os valores é {s}')
print(f'Você digitou {q} números')
