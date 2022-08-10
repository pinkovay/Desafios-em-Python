loja = ('Lápis', 1.75,
        'Estojo', 4.80,
        'Borracha', 0.50,
        'Caderno', 10,
        'Fichário', 17,
        'Mochila', 79.99,
        'Livro', 34.75)
print('_' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('_' * 40)
for pos in range(0, len(loja)):
    if pos % 2 == 0:
        print(f'{loja[pos]:.<30}', end='')
    else:
        print(f'R$ {loja[pos]:.2f}')
print('_' * 40)

