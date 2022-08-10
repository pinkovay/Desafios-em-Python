import math
ang = float(input('Diga o ângulo:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
#print('é {:.2f}'.format(sen))
print(f'O ângulo de {round(ang, 2)} tem o SENO {sen} ')
print(f'O ângulo de {ang} tem o COSSENO {cos}')
print(f'O âmgulo de {ang} tem a TANGENTE de {tan}')
