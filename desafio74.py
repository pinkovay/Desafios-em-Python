from random import randint
aleatorio = (randint(0, 10000), randint(0,10000), randint(0,10000), randint(0,10000), randint(0,10000))
print('NÚMERO GERADO ALEATORIAMENTE)')
print(aleatorio)
print('')
print('Do maior para o menor fica: ', (sorted(aleatorio)))


#Útil para quando eu saber a quantidade de coisas dentro da tupla:
print('O menor número é:', (sorted(aleatorio)[0]))
print('O maior é:', (sorted(aleatorio)[4]))


print('')
#O guanabara ensinou essa nova forma:
print(f'O menor valor é {min(aleatorio)}')
print(f'O maior valor foi {max(aleatorio)}')





