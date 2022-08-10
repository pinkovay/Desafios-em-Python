'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

resp = 's'
soma = media = quant = 0
menor = maior = 0
while resp == 's':
    n = float(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
media = soma / quant
print(f'A média de todos os valores digitados é de: {media}')
print(f'Maior valor digitado: {maior} \nMenor valor digitado: {menor}')







