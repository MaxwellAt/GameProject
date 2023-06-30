import pygame


def historia():
        
    if option == 1:
        screen.blit(pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((0 * 32, 0), (32, 32))),
                                (largura_tela, largura_tela)), 
                                ( largura_tela -350 * escala_para_posicoes, altura_tela -40*escala_para_posicoes))
        screen.blit(titleFonte("Historia", True, "WHITE"), 
                    (largura_tela - 170 * escala_para_posicoes, altura_tela + 70 * escala_para_posicoes))
        screen.blit(textFont("Olá, meu nome é Steve. Acabo de perder meu gato.", True, "WHITE"), 
                    (largura_tela - 650 , altura_tela + 500 * escala_para_posicoes))
        screen.blit(textFont("Você poderia me ajudar a encontra-lo?", True, "WHITE"), 
                    (largura_tela - 650 , altura_tela + 550 * escala_para_posicoes))
        screen.blit(dicaFont("Aperte na tecla 'L' para ajudar o steve e 'Q' para voltar ao menu.", True, "ORANGE"), 
                    (largura_tela - 900 , altura_tela + 100 * escala_para_posicoes))
        pygame.draw.polygon(screen, "WHITE", ((550* escala_para_posicoes,600* escala_para_posicoes),
                                            (640* escala_para_posicoes, 490* escala_para_posicoes), 
                                            (1240* escala_para_posicoes+100, 490* escala_para_posicoes), 
                                            (1240* escala_para_posicoes+100, 590* escala_para_posicoes), 
                                            (640* escala_para_posicoes, 590* escala_para_posicoes)), 2)
    else:
        pygame.draw.polygon(screen, "WHITE", ((550* escala_para_posicoes,600* escala_para_posicoes),
                                            (640* escala_para_posicoes, 490* escala_para_posicoes), 
                                            (1240* escala_para_posicoes, 490* escala_para_posicoes), 
                                            (1240* escala_para_posicoes, 590* escala_para_posicoes), 
                                            (640* escala_para_posicoes, 590* escala_para_posicoes)), 2)
    # # fazer o poligono baseado na tela do jogo
    # pygame.draw.polygon(screen, "WHITE", ((550* escala_para_posicoes,600* escala_para_posicoes),
    #                                       (640* escala_para_posicoes, 490* escala_para_posicoes), 
    #                                       (1240* escala_para_posicoes, 490* escala_para_posicoes), 
    #                                       (1240* escala_para_posicoes, 590* escala_para_posicoes), 
    #                                       (640* escala_para_posicoes, 590* escala_para_posicoes)), 2)


    # pygame.draw.rect(screen, "WHITE", (640, 490, 600, 100), 2)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                cena = cenas["primeira_fase"]
            elif event.key == pygame.K_q:
                cena = cenas["menu"]
