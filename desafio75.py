

#Para adicionar informções a tupla, eu havia feito dessa forma:
''''a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
d = int(input('Digite um último número: '))
conjunto = (a, b, c, d)'''


#O guanabara ensinou assim agora:
num = (int(input('Digite o primeiro número: ')),
     int(input('Digite o segundo número: ')), 
     int(input('Digite o terceiro número: ')),
     int(input('Digite um último número: ')))

print(f'Você digitou os números {num}')
print('O valor 9 apareceu:', num.count(9), 'vezes')

if 3 in num:
    print('O valor 3 apareceu na', num.index(3)+1, 'posição')

print(f'Os números pares digitados foram:', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

