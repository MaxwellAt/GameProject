import pygame
import random





pygame.init()

altura_e_largura = [(1280, 720), (640, 480), (320, 240)]

option = 1
largura_tela, altura_tela = altura_e_largura[option][0], altura_e_largura[option][1]

scala_tranform = (128,128)
if largura_tela < 1280:
    scala_tranform = (64,64)
elif largura_tela < 640:
    scala_tranform = (32,32)
elif largura_tela < 320:
    scala_tranform = (8,8)

escala_para_posicoes = scala_tranform[1]*0.01


screen = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Sabe onde eu estou ? S.O.E.E.")
# pygame.display.set_caption("KWIA ?")
clock = pygame.time.Clock()
running = True
pontos = 0


titleFonte = pygame.font.Font(None, scala_tranform[0]//2).render
textFont = pygame.font.Font(None, scala_tranform[0]//2).render
dicaFont = pygame.font.Font(None, scala_tranform[0]//2).render

allSprites_group = pygame.sprite.Group()



class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens = []
        self.animation = "parado"
        personagem_imagem = pygame.image.load("Assets/Player/Idle.png").convert_alpha()
        personagem_gun = pygame.image.load("Assets/Player/Shoot.png").convert_alpha()
        self.tiroDireita = [
            pygame.transform.scale(personagem_gun.subsurface(pygame.Rect((2 * 32, 64), (32, 32))),scala_tranform),
            pygame.transform.scale(personagem_gun.subsurface(pygame.Rect((3 * 32, 64), (32, 32))),scala_tranform),
        ]
        self.tiroEsquerda = [
            pygame.transform.scale(personagem_gun.subsurface(pygame.Rect((2 * 32, 96), (32, 32))),scala_tranform),
            pygame.transform.scale(personagem_gun.subsurface(pygame.Rect((3 * 32, 96), (32, 32))),scala_tranform),
        ]
        for i in range(2):
            img = personagem_imagem.subsurface(pygame.Rect((i * 32, 0), (32, 32)))
            img = pygame.transform.scale(img, scala_tranform)
            self.imagens.append(img)
        self.index_lista = 0
        self.image = self.imagens[self.index_lista]

        self.ImagemParaDireita = []
        for i in range(2):
            img = personagem_imagem.subsurface(pygame.Rect((i * 32, 64), (32, 32)))
            img = pygame.transform.scale(img, scala_tranform)
            self.ImagemParaDireita.append(img)
        self.index_lista = 0
        self.image = self.ImagemParaDireita[self.index_lista]

        self.ImagemParaEsquerda = []
        for i in range(2):
            img = personagem_imagem.subsurface(pygame.Rect((i * 32, 96), (32, 32)))
            img = pygame.transform.scale(img, scala_tranform)
            self.ImagemParaEsquerda.append(img)
        self.index_lista = 0
        self.image = self.ImagemParaEsquerda[self.index_lista]


        self.rect = self.image.get_rect()
        self.rect.center = (100 * escala_para_posicoes , altura_tela - (100* escala_para_posicoes))

    def update(self):
        velocidade_animation = 0.2
        if self.animation == "parado":
            if self.index_lista >= len(self.imagens) - 1:
                self.index_lista = 0
            else:
                self.index_lista += velocidade_animation
            self.image = self.imagens[int(self.index_lista)]
        elif self.animation == "direita":
            if self.index_lista >= len(self.ImagemParaDireita) - 1:
                self.index_lista = 0
            else:
                self.index_lista += velocidade_animation
            self.image = self.ImagemParaDireita[int(self.index_lista)]
        elif self.animation == "tiro_direita":
            if self.index_lista >= len(self.tiroDireita) - 1:
                self.index_lista = 0
            else:
                self.index_lista += velocidade_animation
            self.image = self.tiroDireita[int(self.index_lista)]
        elif self.animation == "tiro_esquerda":
            if self.index_lista >= len(self.tiroEsquerda) - 1:
                self.index_lista = 0
            else:
                self.index_lista += velocidade_animation
            self.image = self.tiroEsquerda[int(self.index_lista)]
        elif self.animation == "esquerda":
            if self.index_lista >= len(self.ImagemParaEsquerda) - 1:
                self.index_lista = 0
            else:
                self.index_lista += velocidade_animation
            self.image = self.ImagemParaEsquerda[int(self.index_lista)]

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

        # if self.rect.y > altura_tela - 100:
        #     self.rect.y = 500

personagem = Personagem()

class Tiro(pygame.sprite.Sprite):
    def __init__(self,direcao):
        pygame.sprite.Sprite.__init__(self)
        tiro_imagem = pygame.image.load("Assets/Primeira fase/Pixel_Enemy_Platformer/Bullet_Orc_B.png").convert_alpha()
        self.direction = direcao
        self.imagens = []
        for i in range(1):
            img = tiro_imagem.subsurface(pygame.Rect((0, i * 32), (32, 32)))
            img = pygame.transform.scale(img, (scala_tranform[1]//4, scala_tranform[1]//4))
            self.imagens.append(img)
        self.index_lista = 0
        self.image = self.imagens[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (largura_tela - 100, altura_tela - 100)
        # Achar um bom som para o tiro
        pygame.mixer.music.load("Assets/Music/bala.mp3")
        pygame.mixer.music.play()

    def update(self):
        # Ele tem que eliminar a sprit que ele colidiu
        if pygame.sprite.collide_rect(self, inimigo):
            inimigo.kill()
            allSprites_group.remove(self)
            allSprites_group.remove(inimigo)
            global pontos
            pontos += 1
            # if pontos < 20:
            #     inimigo.kill()
            #     allSprites_group.add(inimigo)
            #     allSprites_group.add(inimigo)
        if self.rect.x > largura_tela or self.rect.x < 0 or self.rect.y > altura_tela or self.rect.y < 0:
            allSprites_group.remove(self)
        if self.direction == "direita":
            self.rect.x +=10
        elif self.direction == "esquerda":
            self.rect.x -=10

class Lifebar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        lifeBar = pygame.image.load("Assets/Pixel UI pack 3/06.png").convert_alpha()
        self.imagens = []
        for i in range(4):
            img = lifeBar.subsurface(pygame.Rect((i * 32, 32), (32+16, 16)))
            img = pygame.transform.scale(img, scala_tranform)
            self.imagens.append(img)
        self.index_lista = 0
        self.image = self.imagens[self.index_lista]

        self.rect = self.image.get_rect()
        self.rect.center = (100 * escala_para_posicoes, 40 * escala_para_posicoes)
        self.colisoes = 0

    def update(self):
        if self.colisoes>=1 and self.colisoes<4:
            if self.index_lista >= len(self.imagens) - 1:
                self.index_lista = 0
            self.index_lista += 1
            self.image = self.imagens[self.index_lista]
            personagem.rect.x -= 90
            inimigo.kill()
            allSprites_group.remove(inimigo)
        if self.colisoes >= 4:
            self.colisoes = 0
            personagem.rect.x -= 90
lifebar = Lifebar()

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        inimigo_imagem = pygame.image.load("Assets/Primeira fase/Pixel_Enemy_Platformer/Orc_Big.png").convert_alpha()
        tipo = random.choice(["orc", "zombie"])
        self.imagens = []
        if tipo == "orc":
            inimigo_imagem = pygame.image.load("Assets/Primeira fase/Pixel_Enemy_Platformer/Orc_Big.png").convert_alpha()
            for i in range(3):
                img = inimigo_imagem.subsurface(pygame.Rect((0, i * 32), (64, 32)))
                img = pygame.transform.scale(img, scala_tranform)
                self.imagens.append(img)
        elif tipo == "zombie":
            inimigo_imagem = pygame.image.load("Assets/Primeira fase/Pixel_Enemy_Platformer/Zombie_Big.png").convert_alpha()
            for i in range(3):
                img = inimigo_imagem.subsurface(pygame.Rect(( 32, i * 32), (32, 32)))
                img = pygame.transform.scale(img, scala_tranform)
                self.imagens.append(img)
        elif tipo == "Skeleton":
            # Corrigir depois
            inimigo_imagem = pygame.image.load("Assets/Primeira fase/Pixel_Enemy_Platformer/Skeleton_Big.png").convert_alpha()
            for i in range(8):
                img = inimigo_imagem.subsurface(pygame.Rect(( i * 47,  32/2+5), (32, 32)))
                img = pygame.transform.scale(img, scala_tranform)
                self.imagens.append(img)
        
        self.index_lista = 0
        self.image = self.imagens[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (largura_tela - (100 * escala_para_posicoes), altura_tela - (100 * escala_para_posicoes ) )

    def update(self):
        if pygame.sprite.collide_rect(self,personagem):
            lifebar.colisoes+=1
        if self.index_lista >= len(self.imagens) - 1:
            self.index_lista = 0    
        else:
            self.index_lista += 0.25

        self.image = self.imagens[int(self.index_lista)]

inimigo = Inimigo()

class PauseButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        playbutton = pygame.image.load("Assets/Lucid V1.2/PNG/Flat/64/Pause.png")
        playbutton = pygame.transform.scale(playbutton, (scala_tranform[1]//4, scala_tranform[1]//4))
        self.image = playbutton
        self.rect = self.image.get_rect()
        self.rect.center = ((largura_tela//2)-10 * escala_para_posicoes, 25 *  escala_para_posicoes)
    
    def update(self):
        self.rect.center = ((largura_tela//2)-10, 25)
        for event in pygame.event.get():
            # Corrigir.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.mouse.get_pos()[0] > ((largura_tela//2)-10) and pygame.mouse.get_pos()[0] < ((largura_tela//2)-10)+32:
                        if pygame.mouse.get_pos()[1] > 25 and pygame.mouse.get_pos()[1] < 25+32:
                            print("pause")
                            cena = 1
botaoPause = PauseButton()


class arma(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/gun.jpg").convert_alpha().subsurface(pygame.Rect((0, 0), (32, 32))) # achar uma boa imagem para ser a arma
        self.image = pygame.transform.scale(self.image, scala_tranform)
        self.rect = self.image.get_rect()
        self.rect.center = (largura_tela - 100, altura_tela - 100)
    
    def update(self):
        self.rect.center = (largura_tela - 100, altura_tela + 100)
        if pygame.sprite.collide_rect(self, personagem):
            self.rect.center = personagem.rect.center
        else:
            self.rect.center = (largura_tela - 100, altura_tela - 100)



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
        if cena>= 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.mouse.get_pos()[0] > ((largura_tela//2)-10) and pygame.mouse.get_pos()[0] < ((largura_tela//2)-10)+32:
                        if pygame.mouse.get_pos()[1] > 25 and pygame.mouse.get_pos()[1] < 25+32:
                            cena = 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    cena = 0
                    pontos = 0





    screen.fill("black")



    if cena == cenas["menu"]:        
            
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
    elif cena == cenas["config"]:
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



    elif cena == cenas["historia"]:
        personagem_imagem = pygame.image.load("Assets/Player/Idle.png").convert_alpha()
        screen.blit(pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((0 * 32, 0), (32, 32))),
                                           (largura_tela, largura_tela)), 
                                           (-350* escala_para_posicoes, -40*escala_para_posicoes))
        screen.blit(titleFonte("Historia", True, "WHITE"), 
                    (170 * escala_para_posicoes, 70 * escala_para_posicoes))
        screen.blit(textFont("Olá, meu nome é Steve. Acabo de perder meu gato.", True, "WHITE"), 
                    (650 * escala_para_posicoes, 500 * escala_para_posicoes))
        screen.blit(textFont("Você poderia me ajudar a encontra-lo?", True, "WHITE"), 
                    (650 * escala_para_posicoes, 550 * escala_para_posicoes))
        screen.blit(dicaFont("Aperte na tecla 'L' para ajudar o steve e 'Q' para voltar ao menu.", True, "ORANGE"), 
                    (900 * escala_para_posicoes, 100 * escala_para_posicoes))
        # desenhar uma caixa de dialogo em volta do texto com poligono

        
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
    elif cena == cenas["primeira_fase"]:

        if pontos == 1:
            screen.blit(titleFonte("Parabéns, você aprendeu a atirar", True, "WHITE"), ((largura_tela // 2 - 200) * escala_para_posicoes, (altura_tela // 2 - 100) * escala_para_posicoes ))
            screen.blit(textFont("Aperte na tecla 'L' para continuar", True, "WHITE"), ((largura_tela // 2 - 200) * escala_para_posicoes, (altura_tela // 2 - 50) * escala_para_posicoes))
            # allSprites_group.clear(screen,screen)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        pontos += 1
            # allSprites_group.update()
            # allSprites_group.draw(screen)
        elif pontos >= 2:
            PrimeiraFase(pontos*2)
            allSprites_group.update()
            allSprites_group.draw(screen)
        if pontos == 0:
            PrimeiraFase()
            allSprites_group.update()
            allSprites_group.draw(screen)


    pygame.display.flip()


    clock.tick(num_frame) # fps

pygame.quit()