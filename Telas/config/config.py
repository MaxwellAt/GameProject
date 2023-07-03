import pygame
from .drawConfig import drawConfig

def config(tela,dimensoes,escala,cenas,music):

    largura_tela, altura_tela = dimensoes[0], dimensoes[1]
    centro = {
        "x": largura_tela // 2,
        "y": altura_tela // 2
    }
    
    textFont = pygame.font.Font(None, escala//2).render
    
    textos = {
        "tamanho": textFont("Tamanhos de tela", True, "WHITE"),
        "musica": textFont(f"Musica: {music}", True, "WHITE"),
        "dica": textFont("Aperte na tecla 'Q' para voltar ao menu", True, "WHITE"),
        "1280x720": textFont("1280x720", True, "WHITE"),
        "640x480": textFont("640x480", True, "WHITE"),
        "320x240": textFont("320x240", True, "WHITE")
    }

    botoes = {
        "1280x720":{
                "x0":(largura_tela - centro["x"])//2,
                "x": (largura_tela - centro["x"])//2 + largura_tela // 2,
                "y0": centro["y"] - escala,
                "y": centro["y"] - escala + altura_tela//10
        },
        "640x480":{
                "x0":(largura_tela - centro["x"])//2,
                "x": (largura_tela - centro["x"])//2 + largura_tela // 2,
                "y0": centro["y"],
                "y": centro["y"] + altura_tela//10
        },
        "320x240":{
                "x0":(largura_tela - centro["x"])//2,
                "x": (largura_tela - centro["x"])//2 + largura_tela // 2,
                "y0": centro["y"] + escala ,
                "y": centro["y"] + escala + altura_tela//10
        },
        "musica":{
                "x0":(largura_tela - centro["x"])//2,
                "x": (largura_tela - centro["x"])//2 + largura_tela // 2,
                "y0": textos["musica"].get_height() + altura_tela - escala * 1.5,
                "y": textos["musica"].get_height() + altura_tela - escala * 1.5 + altura_tela//10
        }
    }

    drawConfig(tela,dimensoes,escala,music)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                cenas["config"] = False
                cenas["menu"] = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if botoes["1280x720"]["x0"] <= event.pos[0] <= botoes["1280x720"]["x"] and botoes["1280x720"]["y0"] <= event.pos[1] <= botoes["1280x720"]["y"]:
                    dimensoes = (1280, 720)
                    pygame.display.set_mode(dimensoes)
                    print(dimensoes)
                elif botoes["640x480"]["x0"] <= event.pos[0] <= botoes["640x480"]["x"] and botoes["640x480"]["y0"] <= event.pos[1] <= botoes["640x480"]["y"]:
                    dimensoes = (640, 480)
                    pygame.display.set_mode(dimensoes)
                    print(dimensoes)
                elif botoes["320x240"]["x0"] <= event.pos[0] <= botoes["320x240"]["x"] and botoes["320x240"]["y0"] <= event.pos[1] <= botoes["320x240"]["y"]:
                    dimensoes = (320, 240)
                    pygame.display.set_mode(dimensoes)
                    print(dimensoes)
                elif botoes["musica"]["x0"] <= event.pos[0] <= botoes["musica"]["x"] and botoes["musica"]["y0"] <= event.pos[1] <= botoes["musica"]["y"]:
                    music = not music
    return dimensoes, music