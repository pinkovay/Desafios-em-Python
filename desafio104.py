def leiaInt(msg):
    ok = False
    valor = 0
    while 1:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[31mERRO!!\033[m')
        if ok:
            return valor


num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}')


