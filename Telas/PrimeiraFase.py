import pygame


def primeira_Fase(screen):
    if pontos == 1:
    screen.blit(titleFonte("Parabéns, você aprendeu a atirar", True, "WHITE"), ((largura_tela // 2 - 200) * escala_para_posicoes, (altura_tela // 2 - 100) * escala_para_posicoes ))
    screen.blit(textFont("Aperte na tecla 'L' para continuar", True, "WHITE"), ((largura_tela // 2 - 200) * escala_para_posicoes, (altura_tela // 2 - 50) * escala_para_posicoes))
    # allSprites_group.clear(screen,screen)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                pontos += 1
    elif pontos >= 2:
        PrimeiraFase(pontos*2)
        allSprites_group.update()
        allSprites_group.draw(screen)
    if pontos == 0:
        PrimeiraFase()
        allSprites_group.update()
        allSprites_group.draw(screen)