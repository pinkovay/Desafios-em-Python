s = cont = r = 0
'''s = 0
cont = 0
r = 0'''
while s != 999:
    s = float(input('Digite um número [999 pra parar]: '))
    r = s + r
    cont += 1

print(f'Você digitou {cont - 1} números, e a soma de todos os valores é: {r - 999}')
