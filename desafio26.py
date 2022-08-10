import playsound
import random
from time import sleep
n = str(input('HUMMMM..., pensei em um número aqui, está a fim de tentar acertar qual foi? ')).upper().strip()
if n == 'SIM':
    n1 = int(input('Ok brabão, de 0 a 5, em qual número estou pensando? '))
    lis = [0, 1, 2, 3, 4, 5]
    n2 = random.choice(lis)
    if n1 == n2:
        print('===' * 20)
        print('HUMMMMMM.....')
        sleep(1)
        print(f'Parabéns!!!, eu realmente pensei no {n1}')
        playsound.playsound('acertou.mp3')
    else:
        print('===' * 20)
        print('HUMMMMMM.....')
        sleep(1)
        print(f'Você perdeu!!, pensei no número {n2}')
        playsound.playsound('Errou!!!.mp3')
else:
    print('Tudo bem, quem sabe da proxima vez você queira.')
