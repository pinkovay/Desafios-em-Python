print('-='*20)
print('ANALISADOR DE TRIÃNGULO 2.0')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2+r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima, PODEM formar um triãngulo')
    if r1 == r2 and r2 == r3:
        print('Formará um triângulo EQUILÁTERO')
    elif r1 == r2 and r3 != r2 and r3 != r1 or r2 == r3 and r2 != r1 and r2 != r3 or r3 == r1 and r2 != r1 and r2 != r3 or r3 == r2 and r1 != r2 and r1 != r3:
        print('Formará um triângulo ISÓSCELES ')
    else:
        print('Formará um triângulo ESCALENO')
else:
    print('Os segmentos acima, NÃO PODEM formar um triãngulo')
