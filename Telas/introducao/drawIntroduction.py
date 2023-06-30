import pygame


def drawIntroduction(tela,dimensoes,escala):

    largura_tela, altura_tela = dimensoes[0], dimensoes[1]

    titleFonte = pygame.font.Font(None, escala).render
    textFont = pygame.font.Font(None, escala//3).render
    dicaFont = pygame.font.Font(None, escala//6).render

    centro = {
        "x": largura_tela // 2,
        "y": altura_tela // 2
    }

    textos = {
        "historia": {
            "titulo": titleFonte("Historia", True, "WHITE"),
            "texto": [
                textFont("Olá, meu nome é Steve. Acabo de perder meu gato.", True, "WHITE"),
                textFont("Você poderia me ajudar a encontra-lo?", True, "WHITE")
            ],
            "dica": dicaFont("Aperte na tecla 'L' para ajudar o steve e 'Q' para voltar ao menu.", True, "ORANGE")
        }
    }



    personagem_imagem = pygame.image.load("Assets/Player/Idle.png").convert_alpha()
    personagem_imagem = personagem_imagem.subsurface(pygame.Rect((0 * 32, 0), (32, 32)))
    personagem_imagem = pygame.transform.scale(personagem_imagem, (escala, escala))
    personagem_imagem = pygame.transform.scale(personagem_imagem, (largura_tela, altura_tela))


    tela.blit(textos["historia"]["titulo"],(
        centro["x"] - textos["historia"]["titulo"].get_width()//2,
        escala * 0.25
    ))


    tela.blit(personagem_imagem,(
        personagem_imagem.get_width() - personagem_imagem.get_width() * 1.5,
        personagem_imagem.get_height() - personagem_imagem.get_height() * 0.75
    ))
    

    tela.blit(textos["historia"]["texto"][0], (
        personagem_imagem.get_width() - personagem_imagem.get_width() * 0.75,
        personagem_imagem.get_height() - personagem_imagem.get_height() * 0.25
    ))
    tela.blit(textos["historia"]["texto"][1], (
        personagem_imagem.get_width() - personagem_imagem.get_width() * 0.75,
        personagem_imagem.get_height() - personagem_imagem.get_height() * 0.15
    ))
    tela.blit(textos["historia"]["dica"], (
        personagem_imagem.get_width() - textos["historia"]["dica"].get_width(),
        personagem_imagem.get_height() - personagem_imagem.get_height() * 1
    ))

    # desenhar uma caixa de dialogo em volta do texto com poligono
    pygame.draw.polygon(tela, "WHITE", (
        (escala - escala * 0.75, personagem_imagem.get_height() - personagem_imagem.get_height() * 0.15 + textos["historia"]["texto"][1].get_height()),
        ( personagem_imagem.get_width() - personagem_imagem.get_width() * 0.75 , personagem_imagem.get_height() - personagem_imagem.get_height() * 0.15 + textos["historia"]["texto"][1].get_height()),
        ( personagem_imagem.get_width() - personagem_imagem.get_width() * 0.75 + textos["historia"]["texto"][0].get_width() , personagem_imagem.get_height() - personagem_imagem.get_height() * 0.15 + textos["historia"]["texto"][1].get_height()),
        ( personagem_imagem.get_width() - personagem_imagem.get_width() * 0.75 + textos["historia"]["texto"][0].get_width(), personagem_imagem.get_height() - personagem_imagem.get_height() * 0.25),
        ( personagem_imagem.get_width() - personagem_imagem.get_width() * 0.75 , personagem_imagem.get_height() - personagem_imagem.get_height() * 0.25)
    ), 2)
