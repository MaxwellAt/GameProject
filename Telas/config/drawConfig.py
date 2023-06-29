import pygame

def drawConfig(tela,dimensoes,escala,music=True):

    #########################

    largura_tela, altura_tela = dimensoes[0], dimensoes[1]

    titleFonte = pygame.font.Font(None, escala).render
    textFont = pygame.font.Font(None, escala//2).render

    centro = {
        "x": largura_tela // 2,
        "y": altura_tela // 2
    }

    #########################

    titulo = titleFonte("Configurações", True, "WHITE") # "Configurações TITLE"
    textos = {
        "tamanho": textFont("Tamanhos de tela", True, "WHITE"),
        "musica": textFont(f"Musica: {music}", True, "WHITE"),
        "dica": textFont("Aperte na tecla 'Q' para voltar ao menu", True, "WHITE"),
        "1280x720": textFont("1280x720", True, "WHITE"),
        "640x480": textFont("640x480", True, "WHITE"),
        "320x240": textFont("320x240", True, "WHITE")
    }

    tela.blit(titulo,(
        centro["x"] - titulo.get_width()//2,
        escala * 0.25
    ))


    # tela.blit(titleFonte("Configurações", True, "WHITE"), ((largura_tela // 2)-170, (altura_tela // 2)-200))
    tela.blit(textos["dica"], (
        centro["x"] - textos["dica"].get_width()//2,
        titulo.get_height() + escala * 0.25
    ))

    # modificar o tamanho da tela
    tela.blit(textos["tamanho"], (
        centro["x"] - textos["tamanho"].get_width()//2,
        centro["y"] - escala * 1.5
    ))



    tela.blit(textos["1280x720"], (
        centro["x"] - textos["1280x720"].get_width()//2,
        centro["y"] - escala * 0.75
    ))
    pygame.draw.rect(tela, "WHITE", (
        (largura_tela - centro["x"])//2,
        centro["y"] - escala,
        largura_tela // 2, altura_tela//10), 2)

    tela.blit(textos["640x480"], (
        centro["x"] - textos["640x480"].get_width()//2,
        centro["y"] + escala * 0.25
    ))
    pygame.draw.rect(tela, "WHITE", (
        (largura_tela - centro["x"])//2,
        centro["y"],
        largura_tela // 2, altura_tela//10), 2)
    
    tela.blit(textos["320x240"], (
        centro["x"] - textos["320x240"].get_width()//2,
        centro["y"] + escala * 1.25
    ))
    pygame.draw.rect(tela, "WHITE", (
        (largura_tela - centro["x"])//2,
        centro["y"] + escala,
        largura_tela // 2, altura_tela//10), 2)



    music_symbol = pygame.image.load("./Assets/Lucid V1.2/PNG/Flat/64/Music-0.png")
    music_symbol = pygame.transform.scale(music_symbol, (escala//2, escala//2))

    tela.blit(music_symbol, (
        centro["x"] - textos["musica"].get_width()//2 - escala,
        textos["musica"].get_height() + altura_tela - escala * 1.4
    ))
    tela.blit(textos["musica"], (
        centro["x"] - textos["musica"].get_width()//2,
        textos["musica"].get_height() + altura_tela - escala * 1.25
    ))
    pygame.draw.rect(tela, "WHITE", (
        (largura_tela - centro["x"])//2,
        textos["musica"].get_height() + altura_tela - escala * 1.5,
    largura_tela//2, altura_tela//10), 2)