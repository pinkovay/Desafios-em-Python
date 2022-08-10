import pygame
print('==' * 40)
print('\033[7:30:41mPROGRAMA CRIADO PARA APROVAÇÃO DE EMPRÉSTIMO.\033[m')
print('==' * 40)
valor = float(input('\033[34mQual o valor do bem que deseja adquirir? R$'))
salario = float(input('Quanto é o seu salário? R$'))
anos = int(input('Certo, e em quantos anos pretende pagar? \033[m'))
print('==' * 40)
pres2 = valor / (anos * 12)
pres1 = salario * 30 / 100
if pres2 >= pres1:
    print('\033[7:30:41mNEGADO.\033[m')
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('errado.mp3')
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.event.wait()
elif pres2 == salario * 30 / 100:
    print('\033[7:30:41mACEITO, porém está no limite de 30% de seu salário mensal.\033[m')
    print('\033[4;31mVocê pagará {:.2f} por mês\033[m'.format(pres2))
    print('==' * 40)
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('certo.mp3')
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.event.wait()
else:
    print('\033[7:30:41mACEITO.\033[m')
    print('\033[4;31mVocê pagará {:.2f} por mês\033[m'.format(pres2))
    print('==' * 40)
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('certo.mp3')
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.event.wait()


#é preciso o arquivo dá música estar  no mesmo projeto, para que esse código funcione.


'''pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('astrounaut.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()'''
