def Maior(*num):
    maior_numero = 0
    for c, a in enumerate(sequencia):
        print('_' * 40)
        print(f'{sequencia[c]} foram informados {len(sequencia[c])} valores')
        n = 0
        while n <= len(sequencia[c]):
            for v, valor in enumerate(sequencia[c]):
                if v == 0:
                    maior_numero = valor
                if valor > maior_numero:
                    maior_numero = valor
            n += 1
        print(f'E o maior valor é: {maior_numero}')
        maior_numero = 0
        print('_' * 40)


sequencia = ([2, 3, 4, 7, 9], [4, 8, 3, 0], [78, 54, 3], [567, 2334], [])
Maior()
