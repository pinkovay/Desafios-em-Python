#isso é usado para tocar músicas, em jogos e etc.
import pygame
#inicar antes o mixer do pygame, depois em si o pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('astrounaut.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
#Ou podemos usar a forma mais atual, e mais simples que toca apenas músiica pelo jeito
#import playsound
#playsound.playsound('astrounaut.mp3')
