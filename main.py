import pygame
import random

largura_tela = 1280
altura_tela = 720
pygame.init()
screen = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("KWIA ?")
clock = pygame.time.Clock()
running = True
pontos = 0

titleFonte = pygame.font.Font(None, 64).render

def PlayButton():

    #posições das coisas
    playPos = ((largura_tela // 2) + 80, (altura_tela // 2)-80)


    playbutton = pygame.image.load("./Assets/Lucid V1.2/PNG/Flat/64/Play.png")
    playbutton = pygame.transform.scale(playbutton, (64, 64))

    pygame.draw.rect(screen, "WHITE", ((largura_tela // 2) - 190, (altura_tela // 2)-90, 370, 90), 2)


    screen.blit(playbutton, playPos)
    screen.blit(titleFonte("Play Game", True, "WHITE"), ((largura_tela // 2)-170, (altura_tela // 2)-70))





allSprites_group = pygame.sprite.Group()



class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens = []
        self.animation = "parado"
        personagem_imagem = pygame.image.load("Assets/Player/Idle.png").convert_alpha()
        personagem_gun = pygame.image.load("Assets/Player/Shoot.png").convert_alpha()
        self.tiroDireita = [
            pygame.transform.scale(personagem_gun.subsurface(pygame.Rect((2 * 32, 64), (32, 32))),(128, 128)),
            pygame.transform.scale(personagem_gun.subsurface(pygame.Rect((3 * 32, 64), (32, 32))),(128, 128)),
        ]
        self.tiroEsquerda = [
            pygame.transform.scale(personagem_gun.subsurface(pygame.Rect((2 * 32, 96), (32, 32))),(128, 128)),
            pygame.transform.scale(personagem_gun.subsurface(pygame.Rect((3 * 32, 96), (32, 32))),(128, 128)),
        ]
        for i in range(2):
            img = personagem_imagem.subsurface(pygame.Rect((i * 32, 0), (32, 32)))
            img = pygame.transform.scale(img, (128, 128))
            self.imagens.append(img)
        self.index_lista = 0
        self.image = self.imagens[self.index_lista]

        self.ImagemParaDireita = []
        for i in range(2):
            img = personagem_imagem.subsurface(pygame.Rect((i * 32, 64), (32, 32)))
            img = pygame.transform.scale(img, (128, 128))
            self.ImagemParaDireita.append(img)
        self.index_lista = 0
        self.image = self.ImagemParaDireita[self.index_lista]

        self.ImagemParaEsquerda = []
        for i in range(2):
            img = personagem_imagem.subsurface(pygame.Rect((i * 32, 96), (32, 32)))
            img = pygame.transform.scale(img, (128, 128))
            self.ImagemParaEsquerda.append(img)
        self.index_lista = 0
        self.image = self.ImagemParaEsquerda[self.index_lista]


        self.rect = self.image.get_rect()
        self.rect.center = (100,altura_tela - 100)

    def update(self):
        if self.animation == "parado":
            if self.index_lista >= len(self.imagens) - 1:
                self.index_lista = 0
            else:
                self.index_lista += 1
            self.image = self.imagens[self.index_lista]
        elif self.animation == "direita":
            if self.index_lista >= len(self.ImagemParaDireita) - 1:
                self.index_lista = 0
            else:
                self.index_lista += 1
            self.image = self.ImagemParaDireita[self.index_lista]
        elif self.animation == "tiro_direita":
            if self.index_lista >= len(self.tiroDireita) - 1:
                self.index_lista = 0
            else:
                self.index_lista += 1
            self.image = self.tiroDireita[self.index_lista]
        elif self.animation == "tiro_esquerda":
            if self.index_lista >= len(self.tiroEsquerda) - 1:
                self.index_lista = 0
            else:
                self.index_lista += 1
            self.image = self.tiroEsquerda[self.index_lista]
        elif self.animation == "esquerda":
            if self.index_lista >= len(self.ImagemParaEsquerda) - 1:
                self.index_lista = 0
            else:
                self.index_lista += 1
            self.image = self.ImagemParaEsquerda[self.index_lista]

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
                elif event.key == pygame.K_s and self.rect.y < altura_tela - 128:
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
                elif event.key == pygame.K_q:
                    cena = 1
                elif event.key == pygame.K_l:
                    self.rect.y -= 100
                    self.rect.x += 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if self.animation == "tiro_direita":
                        self.animation = "direita"
                    elif self.animation == "tiro_esquerda":
                        self.animation = "esquerda"

        # if self.rect.y > altura_tela - 100:
        #     self.rect.y = 500

        if self.rect.y < 500: # 500 é o chão.  E isso serve para fazer a mecanica de fisica do chaol
            self.rect.y += 10

personagem = Personagem()

class Tiro(pygame.sprite.Sprite):
    def __init__(self,direcao):
        pygame.sprite.Sprite.__init__(self)
        tiro_imagem = pygame.image.load("Assets/Primeira fase/Pixel_Enemy_Platformer/Bullet_Orc_B.png").convert_alpha()
        self.direction = direcao
        self.imagens = []
        for i in range(1):
            img = tiro_imagem.subsurface(pygame.Rect((0, i * 32), (32, 32)))
            img = pygame.transform.scale(img, (32, 32))
            self.imagens.append(img)
        self.index_lista = 0
        self.image = self.imagens[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (largura_tela - 100, altura_tela - 100)

    def update(self):
        # Ele tem que eliminar a sprit que ele colidiu
        if pygame.sprite.collide_rect(self, inimigo):
            inimigo.kill()
            allSprites_group.remove(self)
            global pontos
            pontos += 1
            if pontos < 20:
                others = Inimigo()
                allSprites_group.add(others)
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
            img = pygame.transform.scale(img, (256, 128))
            self.imagens.append(img)
        self.index_lista = 0
        self.image = self.imagens[self.index_lista]

        self.rect = self.image.get_rect()
        self.rect.center = (140, 50)
        self.colisoes = 0

    def update(self):
        if self.colisoes>=1:
            self.index_lista += 1
            self.image = self.imagens[self.index_lista]
            personagem.rect.x -= 50
lifebar = Lifebar()

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        inimigo_imagem = pygame.image.load("Assets/Primeira fase/Pixel_Enemy_Platformer/Orc_Big.png").convert_alpha()
        self.imagens = []
        for i in range(3):
            img = inimigo_imagem.subsurface(pygame.Rect((0, i * 32), (64, 32)))
            img = pygame.transform.scale(img, (128, 128))
            self.imagens.append(img)
        self.index_lista = 0
        self.image = self.imagens[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (largura_tela - 100, altura_tela - 100)

    def update(self):
        if pygame.sprite.collide_rect(self,personagem):
            lifebar.colisoes+=1
        if self.index_lista >= len(self.imagens) - 1:
            self.index_lista = 0
        else:
            self.index_lista += 1
        self.image = self.imagens[self.index_lista]
        self.rect.x += random.randint(-15, 1)
        self.rect.y += random.randint(-2, 2)

        # if self.rect.x > 600:
        #     self.rect.x = 600

        if self.rect.y < 500: # 500 é o chão.  E isso serve para fazer a mecanica de fisica do chaol
            self.rect.y += 10
        elif self.rect.y > altura_tela:
            self.rect.y = 500

        # if self.rect.x < 0:
        #     self.rect.x = 0

inimigo = Inimigo()

class PauseButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        playbutton = pygame.image.load("Assets/Lucid V1.2/PNG/Flat/64/Play.png")
        playbutton = pygame.transform.scale(playbutton, (32, 32))
        self.image = playbutton
        self.rect = self.image.get_rect()
        self.rect.center = ((largura_tela//2)-10, 25)
    
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


def PrimeiraFase():
    global pontos
    global cena
    # Criar o primeiro cenario
    background = pygame.image.load("./Assets/Primeira fase/Background/Background Props.png")
    background = pygame.transform.scale(background, (largura_tela, altura_tela))
    #definir o background
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, "GREY", (0, 600, largura_tela, 120))
    screen.blit(titleFonte(f"Pontos: {pontos}", True, "WHITE"), (largura_tela - 210,10))

    
    allSprites_group.add(personagem)

    allSprites_group.add(lifebar)

    allSprites_group.add(inimigo)

    allSprites_group.add(botaoPause)

    if pontos >= 20:
        allSprites_group.empty()
        screen.blit(titleFonte("Parabéns, você passou de fase", True, "WHITE"), (largura_tela // 2 - 400, altura_tela // 2 - 100))
        # cena = 3
        screen.blit(titleFonte("Infelizmente não ha mais fases", True, "WHITE"), (largura_tela // 2 - 300, altura_tela // 2 - 50))
        screen.blit(titleFonte("Aperte na tecla 'Q' para voltar ao menu", True, "WHITE"), (largura_tela // 2 - 250, altura_tela // 2))
        # pontos = 0

    # colocar a pontuação na tela


num_frame = 30
cena = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if cena == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.mouse.get_pos()[0] > (largura_tela // 2) - 190 and pygame.mouse.get_pos()[0] < (largura_tela // 2) + 180:
                        if pygame.mouse.get_pos()[1] > (altura_tela // 2) - 90 and pygame.mouse.get_pos()[1] < (altura_tela // 2) + 0:
                            cena = 2
        # elif cena >= 2:
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if event.button == 1:
        #             if pygame.mouse.get_pos()[0] > ((largura_tela//2)-10) and pygame.mouse.get_pos()[0] < ((largura_tela//2)-10)+32:
        #                 if pygame.mouse.get_pos()[1] > 25 and pygame.mouse.get_pos()[1] < 25+32:
        #                     cena = 1






    screen.fill("black")


    if cena == 1:
        PlayButton()
    elif cena == 2:
        PrimeiraFase()
        allSprites_group.update()
        allSprites_group.draw(screen)

    pygame.display.flip()


    clock.tick(num_frame) # fps

pygame.quit()