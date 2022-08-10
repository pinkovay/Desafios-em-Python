lista = list()
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('')
print(f'O maior valor digitado foi {maior}, na posição: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print('')
print(f'O menor foi {menor}, na posição: ', end='')
for a, d in enumerate(lista):
    if d == menor:
        print(f'{a}...', end='')
