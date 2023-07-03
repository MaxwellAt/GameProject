import pygame
from Objetos import *
import random

class primeiraFase:
    def __init__(self,screen,dimensoes,escala):
        self.pontos = 0
        self.screen = screen
        self.dimensoes = dimensoes
        self.escala = escala
        
        self.allSprites_group = pygame.sprite.Group() # -> Grupo de Sprits

        
        self.lifebar = Lifebar((escala  ,escala))
        self.inimigo = Inimigo((escala,escala))
        self.inimigos = [self.inimigo]
        self.personagem = Personagem((escala,escala),self.allSprites_group,self.inimigos)

        self.allSprites_group.add(self.personagem)

        self.allSprites_group.add(self.lifebar)

        self.allSprites_group.add(self.inimigo)        

        largura_tela, altura_tela = dimensoes[0], dimensoes[1]

        self.lifebar.rect.center = (escala, escala * 0.5)
        self.personagem.rect.center = (escala * 0.5, altura_tela - (escala * 0.5))
        self.inimigo.rect.center = (largura_tela - escala * 0.75,altura_tela - escala * 0.75)



    
    def draw(self,cenas):



        screen = self.screen
        escala = self.escala
        dimensoes = self.dimensoes
        largura_tela, altura_tela = dimensoes[0], dimensoes[1]

        pause = pygame.image.load("./Assets/Lucid V1.2/PNG/Flat/64/Pause.png").convert_alpha()
        pause = pygame.transform.scale(pause, (escala//4, escala//4))
        pause = pause.subsurface((0, 0, escala//4, escala//4))

        titleFonte = pygame.font.Font(None, escala).render
        textFont = pygame.font.Font(None, escala//2).render

        centro = {
            "x": largura_tela // 2,
            "y": altura_tela // 2
        }


        # Criar o primeiro cenario
        background = pygame.image.load("./Assets/Primeira fase/Background/Background Props.png")
        background = pygame.transform.scale(background, (largura_tela, altura_tela))
        
        pontuacao = textFont(f"Pontos: {self.pontos}", True, "WHITE")
        
        #definir o background
        screen.blit(background, (0, 0))
        # plataforma
        plataforma_pos = (0, altura_tela - 50, largura_tela, 100 * escala)
        pygame.draw.rect(screen, "GREY", plataforma_pos)

        screen.blit(pontuacao, (
            largura_tela - pontuacao.get_width() - escala//4,
            escala * 0.5 - pontuacao.get_height()//2
        ))

        screen.blit(pause, (
            centro["x"] - pause.get_width()//2,
            escala * 0.5 - pause.get_height()//2
        ))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if pause.get_rect(center=(centro["x"], escala * 0.5)).collidepoint(mouse_pos):
                    cenas["pause"] = True
                    cenas["primeira_fase"] = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.personagem.animation == "direita":
                        self.personagem.animation = "tiro_direita"
                        tiro = Tiro("direita",self.personagem.inimigos)
                        self.personagem.allSprites_group.add(tiro)
                        tiro.rect.center = self.personagem.rect.center

                    elif self.personagem.animation == "esquerda":
                        self.personagem.animation = "tiro_esquerda"
                        tiro = Tiro("esquerda",self.personagem.inimigos)
                        self.personagem.allSprites_group.add(tiro)
                        tiro.rect.center = self.personagem.rect.center
                        

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if self.personagem.animation == "tiro_direita":
                        self.personagem.animation = "direita"
                    elif self.personagem.animation == "tiro_esquerda":
                        self.personagem.animation = "esquerda"

        pass

    def update(self,cenas):
        self.draw(cenas)

        if len(self.inimigos) == 0:
            self.pontos += 1
            for i in range(self.pontos * 2):
                self.inimigo = Inimigo((self.escala,self.escala))
                self.inimigo.rect.center = (
                    random.randint(int(self.dimensoes[0]//2), int(self.dimensoes[0])),
                    self.dimensoes[1] - self.escala * random.choice([0.5,0.75,1])
                )
                self.inimigos.append(self.inimigo)
                self.allSprites_group.add(self.inimigo)
                self.allSprites_group.update()

        self.allSprites_group.update()
        self.allSprites_group.draw(self.screen)

        # if pygame.sprite.collide_rect(self.personagem, self.inimigo):
        #     self.pontos += 1
        #     self.inimigo.rect.center = (self.dimensoes[0] - (random.randint(-10,50) * self.escala), self.dimensoes[1] - (random.randint(0,100) * self.escala ) )
        #     self.allSprites_group.add(self.inimigo)
        #     self.allSprites_group.update()
