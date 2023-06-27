import pygame


def primeira_Fase(screen):

    """

        LOGICA DO PERSONAGEM
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.rect.x -= 10
                    self.animation = "esquerda"
                elif event.key == pygame.K_d:
                    self.rect.x += 10
                    self.animation = "direita"
                elif event.key == pygame.K_w:
                    self.rect.y -= 10
                elif event.key == pygame.K_s and self.rect.y < altura_tela - (128 * escala_para_posicoes):
                    self.rect.y += 10
                elif event.key == pygame.K_SPACE:
                    if self.animation == "direita":
                        self.animation = "tiro_direita"
                        tiro = Tiro(direcao="direita")
                        allSprites_group.add(tiro)
                        tiro.rect.center = self.rect.center
                    elif self.animation == "esquerda":
                        self.animation = "tiro_esquerda"
                        tiro = Tiro(direcao="esquerda")
                        allSprites_group.add(tiro)
                        tiro.rect.center = self.rect.center        
                elif event.key == pygame.K_l:
                    self.rect.y -= (100 * escala_para_posicoes)
                    self.rect.x += (10 * escala_para_posicoes)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if self.animation == "tiro_direita":
                        self.animation = "direita"
                    elif self.animation == "tiro_esquerda":
                        self.animation = "esquerda"
    """


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



        """
def PrimeiraFase(numeroInimigos=1):
    global pontos
    global cena
    # Criar o primeiro cenario
    background = pygame.image.load("./Assets/Primeira fase/Background/Background Props.png")
    background = pygame.transform.scale(background, (largura_tela, altura_tela))
    #definir o background
    screen.blit(background, (0, 0))
    # plataforma
    plataforma_pos = (0, altura_tela - 50, largura_tela, 100 * escala_para_posicoes)
    pygame.draw.rect(screen, "GREY", plataforma_pos)

    screen.blit(titleFonte(f"Pontos: {pontos}", True, "WHITE"), (largura_tela - ( 210 * escala_para_posicoes),10))

    
    allSprites_group.add(personagem)

    allSprites_group.add(lifebar)

    allSprites_group.add(botaoPause)
    
    # gun = arma()
    # allSprites_group.add(gun)


    # mecanica de fisica para manter o personagem na plataforma
    if personagem.rect.center[1] <= altura_tela - (120 * escala_para_posicoes):
        personagem.rect.y += 10


    if pontos < 1 :
        allSprites_group.add(inimigo)
    elif pontos > 0 and pontos < 20:
        for i in range(numeroInimigos):
            inimigo.rect.center = (largura_tela - (random.randint(-10,50) * escala_para_posicoes), altura_tela - (random.randint(0,100) * escala_para_posicoes ) )
            allSprites_group.add(inimigo)
    elif pontos >= 20:
        allSprites_group.empty()
        screen.blit(titleFonte("Parabéns, você passou de fase", True, "WHITE"), ((largura_tela // 2 - 400) * escala_para_posicoes, (altura_tela // 2 - 100) * escala_para_posicoes ))
        # cena = 3
        screen.blit(titleFonte("Infelizmente não ha mais fases", True, "WHITE"), (largura_tela // 2 - 300, altura_tela // 2 - 50))
        screen.blit(titleFonte("Aperte na tecla 'Q' para voltar ao menu", True, "WHITE"), (largura_tela // 2 - 250, altura_tela // 2))

"""
     