
# usando o modo: Importação de biblioteca math
'''from math import factorial
numero = int(input('Digite um número, para calcular seu fatorial: '))
n = factorial(numero)
print(f'O factorial de {numero}, é {n}')'''

# usando o modo: while
'''numero = int(input('Digite um número, para calcular seu fatorial: '))
c = numero
f = 1
print(f'Calculando o {numero}! =', end='')
while c >= 1:
    print(f' {c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(f)'''


# usando o modo: for
numero = int(input('Digite um número para saber seu fatorial:'))
print(f' {numero}', end='')
c = numero
f = 1
for c in range(numero, 1, -1):
    c = c-1
    if c >= 1:
        print(' X', c, end='')
        numero = numero * c
print(f'= {numero}!')







