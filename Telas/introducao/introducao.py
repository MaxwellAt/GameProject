import pygame
from .drawIntroduction import drawIntroduction

def historia(tela,dimensoes,escala,cenas):

    drawIntroduction(tela,dimensoes,escala)

    # pygame.draw.rect(screen, "WHITE", (640, 490, 600, 100), 2)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                cenas["historia"] = False
                cenas["primeira_fase"] = True
            elif event.key == pygame.K_q:
                cenas["historia"] = False
                cenas["menu"] = True
