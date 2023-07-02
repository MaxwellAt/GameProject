import pygame


def drawPauseMenu(tela,dimensoes,escala):

    largura_tela, altura_tela = dimensoes[0], dimensoes[1]

    titleFonte = pygame.font.Font(None, escala).render
    textFont = pygame.font.Font(None, escala//2).render


    centro = {
        "x": largura_tela // 2,
        "y": altura_tela // 2
    }

    titulo = titleFonte("Pause Menu", True, "WHITE") # "KWIA ?"
    subtitulo = textFont("S.O.E.E", True, "WHITE") # "(Know Where I Are?)"

    playbutton = pygame.image.load("./Assets/Lucid V1.2/PNG/Flat/64/Play.png")
    config_button = pygame.image.load("./Assets/Lucid V1.2/PNG/Flat/64/Three-Dots-Horizontal.png")

    playbutton = pygame.transform.scale(playbutton, (escala//2,escala//2))
    config_button = pygame.transform.scale(config_button, (escala//2,escala//2))

    tela.blit(titulo,(
        centro["x"] - titulo.get_width()//2, 
        escala * 0.25
    ))
    
    tela.blit(subtitulo,(
        centro["x"] - subtitulo.get_width()//2,
        (escala * 0.25) + titulo.get_height()
    ))




    tela.blit(playbutton, (
        centro["x"] + escala * 1.5,
        centro["y"] - escala * 0.75
    ))
    
    tela.blit(titleFonte("Resume", True, "WHITE"), ( 
        ((largura_tela - centro["x"])//2) + escala * 0.15,
        centro["y"] - escala * 0.75
    ))

    pygame.draw.rect(tela, "WHITE", (
        (largura_tela - centro["x"])//2,
        centro["y"] - escala * 0.75,
        largura_tela // 2, altura_tela//8), 2)



    tela.blit(config_button, (
        centro["x"] + escala * 1.5,
        centro["y"] + escala * 0.75
    ))
    
    tela.blit(titleFonte("Settings", True, "WHITE"), (
        ((largura_tela - centro["x"])//2) + escala * 0.15,
        centro["y"] + escala * 0.75
    ))
    
    pygame.draw.rect(tela, "WHITE", (
        (largura_tela - centro["x"])//2,
        centro["y"] + escala * 0.75,
        largura_tela // 2, altura_tela//8), 2)