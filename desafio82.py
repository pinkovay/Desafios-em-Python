lista_all = list()
lista_par = list()
lista_imp = list()
while True:
    valor = (int(input('Digite um valor: ')))
    lista_all.append(valor)
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_imp.append(valor)
    con = str(input('Deseja adicionar mais algum valor? [S/N] '))
    if con in 'Nn':
        print('Lista total: ',  lista_all)
        print('Somente números pares: ', lista_par)
        print('Somente números impáres:', lista_imp)

 
