import pygame

def menu():
        playPos = ((largura_tela // 2) + 80, (altura_tela // 2)-80)
        playbutton = pygame.image.load("./Assets/Lucid V1.2/PNG/Flat/64/Play.png")
        playbutton = pygame.transform.scale(playbutton, (scala_tranform[1]//2, scala_tranform[1]//2))

        screen.blit(playbutton, playPos)
        screen.blit(titleFonte("Play Game", True, "WHITE"), ((largura_tela // 2)-170, (altura_tela // 2)-70))
        screen.blit(titleFonte("S.O.E.E.", True, "WHITE"), ((largura_tela // 2)-120, (altura_tela // 2)-200))
        screen.blit(textFont("(Sabe onde eu estou ?)", True, "WHITE"), ((largura_tela // 2)-120, (altura_tela // 2)-150))
        # screen.blit(titleFonte("KWIA ?", True, "WHITE"), ((largura_tela // 2)-120, (altura_tela // 2)-200))
        # screen.blit(textFont("(Know Where I Are?)", True, "WHITE"), ((largura_tela // 2)-120, (altura_tela // 2)-150))
        pygame.draw.rect(screen, "WHITE", ((largura_tela // 2) - 190, (altura_tela // 2)-90, 370, 90), 2)


        config_button = pygame.image.load("./Assets/Lucid V1.2/PNG/Flat/64/Three-Dots-Horizontal.png")
        config_button = pygame.transform.scale(config_button, (scala_tranform[1]//2, scala_tranform[1]//2))
        configPos = ((largura_tela // 2) + 80, (altura_tela // 2)+20)
    
        screen.blit(config_button, configPos)
        screen.blit(titleFonte("Settings", True, "WHITE"), ((largura_tela // 2)-170, configPos[1]+10))
        pygame.draw.rect(screen, "WHITE", ((largura_tela // 2) - 190, configPos[1]-10, 370, 90), 2)

        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.mouse.get_pos()[0] > (largura_tela // 2) - 190 and pygame.mouse.get_pos()[0] < (largura_tela // 2) + 180:
                        if pygame.mouse.get_pos()[1] > (altura_tela // 2) - 90 and pygame.mouse.get_pos()[1] < (altura_tela // 2) + 0:
                            cena = cenas["historia"]
                    if pygame.mouse.get_pos()[0] > (largura_tela//2)-190 and pygame.mouse.get_pos()[0] < (largura_tela//2)+180:
                        if pygame.mouse.get_pos()[1] > (altura_tela//2)-10 and pygame.mouse.get_pos()[1] < (altura_tela//2)+80:
                            cena = cenas["config"]