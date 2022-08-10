from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
#hi = co ** 2 + ca ** 2
#hi1 = hi**(1/2)
#print('O comprimento da hipotenusa é {:.2f}'.format(hi1))
hi = hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))
