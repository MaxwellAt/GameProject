import pygame

def config():
            screen.blit(titleFonte("Configurações", True, "WHITE"), ((largura_tela // 2)-170, (altura_tela // 2)-200))
        screen.blit(textFont("Aperte na tecla 'Q' para voltar ao menu", True, "WHITE"), ((largura_tela // 2)-170, (altura_tela // 2)-150))

        # modificar o tamanho da tela
        screen.blit(titleFonte("Tamanho da tela", True, "WHITE"), ((largura_tela // 2)-170, (altura_tela // 2)-100))
        pygame.draw.rect(screen, "WHITE", ((largura_tela // 2) - 180, (altura_tela // 2)-110, 400, 60*4), 2)

        screen.blit(textFont("1280x720", True, "WHITE"), ((largura_tela // 2)-20, (altura_tela // 2)-40))
        pygame.draw.rect(screen, "WHITE", ((largura_tela // 2) - 180, (altura_tela // 2)-50, 400, 40), 2)

        screen.blit(textFont("640x480", True, "WHITE"), ((largura_tela // 2)-20, (altura_tela // 2)+20))
        pygame.draw.rect(screen, "WHITE", ((largura_tela // 2) - 180, (altura_tela // 2)+10, 400, 40), 2)
        
        screen.blit(textFont("320x240", True, "WHITE"), ((largura_tela // 2)-20, (altura_tela // 2)+80))
        pygame.draw.rect(screen, "WHITE", ((largura_tela // 2) - 180, (altura_tela // 2)+70, 400, 40), 2)


        music_symbol = pygame.image.load("./Assets/Lucid V1.2/PNG/Flat/64/Music-0.png")

        screen.blit(music_symbol, ((largura_tela // 2)-100, (altura_tela // 2)+160))
        screen.blit(textFont(f"Musica: {music}", True, "WHITE"), ((largura_tela // 2)-10, (altura_tela // 2)+180))
        pygame.draw.rect(screen, "WHITE", ((largura_tela // 2) - 180, (altura_tela // 2)+150, 400, 90), 2)


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    cena = cenas["menu"]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.mouse.get_pos()[0] > (largura_tela // 2) - 190 and pygame.mouse.get_pos()[0] < (largura_tela // 2) + 180:
                        if pygame.mouse.get_pos()[1] > (altura_tela // 2) - 90 and pygame.mouse.get_pos()[1] < (altura_tela // 2) + 0:
                            option = 0
                            largura_tela, altura_tela = altura_e_largura[option][0], altura_e_largura[option][1]
                            screen = pygame.display.set_mode((largura_tela, altura_tela))
                            pygame.display.set_caption("Sabe onde eu estou ? S.O.E.E.")
                            running = True
                            pontos = 0
                            cena = cenas["menu"]
                    if pygame.mouse.get_pos()[0] > (largura_tela // 2) - 190 and pygame.mouse.get_pos()[0] < (largura_tela // 2) + 180:
                        if pygame.mouse.get_pos()[1] > (altura_tela // 2) - 40 and pygame.mouse.get_pos()[1] < (altura_tela // 2) + 50:
                            option = 1
                            largura_tela, altura_tela = altura_e_largura[option][0], altura_e_largura[option][1]
                            screen = pygame.display.set_mode((largura_tela, altura_tela))
                            pygame.display.set_caption("Sabe onde eu estou ? S.O.E.E.")
                            running = True
                            pontos = 0
                            cena = cenas["menu"]
                    if pygame.mouse.get_pos()[0] > (largura_tela // 2) - 190 and pygame.mouse.get_pos()[0] < (largura_tela // 2) + 180:
                        if pygame.mouse.get_pos()[1] > (altura_tela // 2) + 20 and pygame.mouse.get_pos()[1] < (altura_tela // 2) + 110:
                            option = 2
                            largura_tela, altura_tela = altura_e_largura[option][0], altura_e_largura[option][1]
                            screen = pygame.display.set_mode((largura_tela, altura_tela))
                            pygame.display.set_caption("Sabe onde eu estou ? S.O.E.E.")
                            running = True
                            pontos = 0
                            cena = cenas["menu"]
                    if pygame.mouse.get_pos() > ((largura_tela // 2)-190, (altura_tela // 2)+140) and pygame.mouse.get_pos() < ((largura_tela // 2)+180, (altura_tela // 2)+230):
                        music = not music
                        print(f"musica {music}")

