import pygame
from .drawIntroduction import drawIntroduction

def historia(tela,dimensoes,escala):

    drawIntroduction(tela,dimensoes,escala)

    # pygame.draw.rect(screen, "WHITE", (640, 490, 600, 100), 2)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                print("proximo")
            elif event.key == pygame.K_q:
                print("voltar")
