n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro: '))
print('==' * 40)
menu = int(input('[1] SOMA\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\nSua escolha: '))
if menu >= 6 or menu <= 0:
    print('==' * 40)
    print('Opção inválida, tente novamente.')
    print('==' * 40)
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro: '))
    menu = int(input('[1] SOMA\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\nSua escolha: '))
if menu == 4:
    while menu == 4:
        print('==' * 40)
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro: '))
        menu = int(input('[1] SOMA\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\nSua escolha: '))
if menu == 1:
    print('==' * 40)
    soma = n1 + n2
    print(f'A soma de {n1} + {n2} é: {soma}')
elif menu == 2:
    print('==' * 40)
    multi = n1 * n2
    print(f'O resultado de {n1} multiplicado por {n2} é: {multi} ')
elif menu == 3:
    if n1 > n2:
        print('==' * 40)
        print(f'Maior número digitado: {n1} ')
    elif n2 > n1:
        print('==' * 40)
        print(f'Maior número digitado: {n2} ')
    elif n2 == n1:
        print('==' * 40)
        print('Os dois números são iguais')
elif menu == 5:
    print('==' * 40)
    print('PROGRAMA FECHADO.')




