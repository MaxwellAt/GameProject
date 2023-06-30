import pygame
# from Objetos import *
from Telas import *

pygame.init()

altura_e_largura = [(1280, 720), (640, 480), (320, 240)]
altura_e_largura = altura_e_largura[0]

escala = altura_e_largura[0]//10

screen = pygame.display.set_mode(altura_e_largura)
pygame.display.set_caption("Sabe onde eu estou ? S.O.E.E.")
clock = pygame.time.Clock()
running = True





# titleFonte = pygame.font.Font(None, 64).render
# textFont = pygame.font.Font(None, 32).render
# dicaFont = pygame.font.Font(None, 16).render

allSprites_group = pygame.sprite.Group() # -> Grupo de Sprits





# music = True
# pygame.mixer.music.load("Assets/Music/Trilha.mp3")
# pygame.mixer.music.play(-1)
    
num_frame = 30
while running:

    # if not music:
    #     pygame.mixer.music.pause()
    # else:
    #     pygame.mixer.music.unpause()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.fill("black")

    # menu(screen,altura_e_largura,escala)
    # config(screen,altura_e_largura,escala)

    historia(screen,altura_e_largura,escala)


    pygame.display.flip()


    clock.tick(num_frame) # fps

pygame.quit()