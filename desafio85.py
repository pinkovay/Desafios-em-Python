
#MODO QUE EU FIZ
"""inteira = list()
par = list()
impar = list()
n = 0
while 1:
    inteira.append(float(input('Digite um valor: ')))
    if inteira[n] % 2 == 0:
        par.append(inteira[n])
    else:
        impar.append(inteira[n])
    n += 1
    con = str(input('Deseja adicionar mais algo? [S/N] '))
    if con in 'Nn':
        break
print('_' * 30)
inteira.sort()
par.sort()
impar.sort()
print(f'Lista total digitada: {inteira}')
print(f'Lista de números pares: {par}')
print(f'Lista de números ímpares: {impar}')
print(f'Lista total digitada: {inteira}')"""



#MODO QUE O PROFESSOR FEZ
núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = float(input('Digite um valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
núm[0].sort()
núm[1].sort()
print(f'Números pares: {núm[0]} ')
print(f'Números ímpares: {núm[1]}')

#OS DOIS MODOS FUNCIONAM PERFEITAMENTE