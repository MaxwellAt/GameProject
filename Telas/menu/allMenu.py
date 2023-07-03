import pygame
from .drawMenu import drawMenu

def menu(screen,dimensoes,escala,cenas):

    largura_tela, altura_tela = dimensoes[0], dimensoes[1]
    centro = {
        "x": largura_tela // 2,
        "y": altura_tela // 2
    }

    playbutton = {
        "x0":(largura_tela - centro["x"])//2,
        "x": ((largura_tela - centro["x"])//2) + largura_tela // 2,
        "y0": centro["y"] - escala * 0.75,
        "y": (centro["y"] - escala * 0.75) + altura_tela//8
    }

    config_button = {
        "x0": (largura_tela - centro["x"])//2,
        "x": ((largura_tela - centro["x"])//2) + largura_tela // 2,
        "y0": centro["y"] + escala * 0.75,
        "y": (centro["y"] + escala * 0.75) + altura_tela//8
    }

    
    drawMenu(screen,dimensoes,escala)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if playbutton["x0"] <= event.pos[0] <= playbutton["x"] and playbutton["y0"] <= event.pos[1] <= playbutton["y"]:
                    cenas["menu"] = False
                    cenas["historia"] = True
                if config_button["x0"] <= event.pos[0] <= config_button["x"] and config_button["y0"] <= event.pos[1] <= config_button["y"]:
                    cenas["menu"] = False
                    cenas["config"] = True
