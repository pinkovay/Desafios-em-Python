n = int(input('\033[31mDiga um número inteiro: '))
conversao = str(input('Deseja converter este número para:\n[1] BINÁRIO\n[2] OCTAL\n[3] HEXADECIMAL\nSua opção: ')).upper().strip()

if conversao == '1':
    binario = format(n, 'b')
    print(f'O número {n} em BINÁRIO fica: {binario}')

elif conversao == '2':
    octal = format(n, 'o')
    print(f'O número {n}, em OCTAL fica: {octal}')

elif conversao == '3':
   print('O número {}, em HEXADECIMAL fica: {}'.format(n, hex(n)[2:]))

else:
    print('Você digitou algo errado, reinicie por favor.')
