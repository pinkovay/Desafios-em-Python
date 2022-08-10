print('-' * 40)
print('LOJA BARATEIA')
print('-' * 40)
soma = mil = contador = 0 #5
menor = 0
nomebarato = ' '
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço: ')) #5
    soma += valor
    contador += 1
    if valor >= 1000:
        mil += 1
    if contador == 1 or valor < menor:
        nomebarato = produto
        menor = valor
    continuacao = ' '
    while continuacao not in 'SN':
        continuacao = str(input('Desejar adicionar mais algo? [S/N')).strip().upper()[0]
    if continuacao == 'N':
        break
print('-' * 10, 'FIM', '-' * 10)
print(f'O total da compra foi R${soma}')
print(f'Temos {mil} produto custando R1000,00 ou mais.')
print(f'O produto mais barato foi: {nomebarato}, que custa R${menor}')


