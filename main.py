import pygame
import random


pygame.init()

altura_e_largura = [(1280, 720), (640, 480), (320, 240)]


screen = pygame.display.set_mode(altura_e_largura[0])
pygame.display.set_caption("Sabe onde eu estou ? S.O.E.E.")
clock = pygame.time.Clock()
running = True
pontos = 0


titleFonte = pygame.font.Font(None, scala_tranform[0]//2).render
textFont = pygame.font.Font(None, scala_tranform[0]//2).render
dicaFont = pygame.font.Font(None, scala_tranform[0]//2).render

allSprites_group = pygame.sprite.Group()



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
        


music = True
pygame.mixer.music.load("Assets/Music/Trilha.mp3")
pygame.mixer.music.play(-1)    
    
num_frame = 30
cenas = {
    "menu": 0,
    "config": 1,
    "historia": 2,
    "primeira_fase": 3,
    "segunda_fase": 4,
}
cena = cenas["historia"]
while running:

    if not music:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





    screen.fill("black")



    # if cena == cenas["menu"]:
    # elif cena == cenas["config"]:
    # elif cena == cenas["historia"]:
    # elif cena == cenas["primeira_fase"]:




    pygame.display.flip()


    clock.tick(num_frame) # fps

pygame.quit()