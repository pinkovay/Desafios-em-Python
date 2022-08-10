
contagem = ('zero', 'um' , 'dois' , 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesste', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 á 20: '))
    while num < 0 or num > 20:
        num = int(input('Digite apenas o intervalo de números pedido: '))
    print(f'Você digitou o número {contagem[num]}')
    confirm = input('Deseja testar novamente? [S/N] ').strip().upper()[0]
    if confirm == 'S':
        print('')
    elif confirm == 'N':
        print('Programa encerrado')
        break


