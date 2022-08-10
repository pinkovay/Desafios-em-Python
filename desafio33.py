n1 = float(input('Diga um número: '))  # 10
n2 = float(input('Diga outro:'))  # 2
n3 = float(input('Agora diga o último: '))  # 3
'''if n1 < n2 and n1 < n3:
    menor = n1
    print(f'O menor é {menor}')
if n2 < n1 and n2 < n3:
    menor = n2
    print(f'O menor é {menor}')
if n3 < n1 and n3 < n2:
    menor = n3
    print(f'O menor é {menor}')

if n1 > n2 and n1 > n3:
    maior = n1
    print(f'O maior é {maior}')
if n2 > n1 and n2 > n3:
    maior = n2
    print(f'O maior é {maior}')
if n3 > n1 and n3 > n2:
    maior = n3
    print(f'O maior é {maior}')'''
# modo mais fácil
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O maior número é: {maior}')
print(f'O menor é: {menor}')
