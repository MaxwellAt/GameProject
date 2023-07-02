import pygame
# from Objetos import *
from Telas import *
from Objetos import *

pygame.init()

altura_e_largura = [(1280, 720), (640, 480), (320, 240)]
altura_e_largura = altura_e_largura[1]

escala = altura_e_largura[0]//10


screen = pygame.display.set_mode(altura_e_largura)
pygame.display.set_caption("Sabe onde eu estou ? S.O.E.E.")
clock = pygame.time.Clock()
running = True




# titleFonte = pygame.font.Font(None, 64).render
# textFont = pygame.font.Font(None, 32).render
# dicaFont = pygame.font.Font(None, 16).render

allSprites_group = pygame.sprite.Group() # -> Grupo de Sprits





music = True
pygame.mixer.music.load("Assets/Music/Trilha.mp3")
pygame.mixer.music.play(-1)

primeira_fase = primeiraFase(screen,altura_e_largura,escala)

num_frame = 30
cenas = {
    "menu": True,
    "config": False,
    "historia": False,
    "pause": False,
    "primeira_fase": False
}
while running:

    if not music:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.fill("black")

    # menu(screen,altura_e_largura,escala)
    # config(screen,altura_e_largura,escala)
    # historia(screen,altura_e_largura,escala)
    # menuPause(screen,altura_e_largura,escala)
    
    if cenas["menu"]:
        menu(screen,altura_e_largura,escala,cenas)
    if cenas["config"]:
        altura_e_largura, music = config(screen,altura_e_largura,escala,cenas, music)
    if cenas["historia"]:
        historia(screen,altura_e_largura,escala,cenas)
    if cenas["pause"]:
        menuPause(screen,altura_e_largura,escala,cenas)
    if cenas["primeira_fase"]:
        primeira_fase.update(cenas)

    # primeira_fase.update()

    pygame.display.flip()


    clock.tick(num_frame) # fps

pygame.quit()