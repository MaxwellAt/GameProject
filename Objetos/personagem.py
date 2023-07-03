import pygame
from .tiro import Tiro

class Personagem(pygame.sprite.Sprite):
    def __init__(self,scala_tranform,allSprites_group,inimigos:list):
        pygame.sprite.Sprite.__init__(self)
        
        self.animation = "parado" # -> Mudar sprit
        self.allSprites_group = allSprites_group
        self.inimigos = inimigos
        self.escala = scala_tranform[0]

        personagem_imagem = pygame.image.load("Assets/Player/Idle.png").convert_alpha()
        personagem_gun = pygame.image.load("Assets/Player/Shoot.png").convert_alpha()
        self.tiro = pygame.image.load("Assets/Primeira fase/Pixel_Enemy_Platformer/Bullet_Orc_B.png").convert_alpha()
        self.tiro = pygame.transform.scale(self.tiro, (16,16))
        
        self.imagens = [
            pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((0 * 32, 0), (32, 32))), scala_tranform),
            pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((1 * 32, 0), (32, 32))), scala_tranform)
        ]

        self.tiroDireita = [
            pygame.transform.scale(personagem_gun.subsurface(pygame.Rect((2 * 32, 64), (32, 32))),scala_tranform),
            pygame.transform.scale(personagem_gun.subsurface(pygame.Rect((3 * 32, 64), (32, 32))),scala_tranform),
        ]
        self.tiroEsquerda = [
            pygame.transform.scale(personagem_gun.subsurface(pygame.Rect((2 * 32, 96), (32, 32))),scala_tranform),
            pygame.transform.scale(personagem_gun.subsurface(pygame.Rect((3 * 32, 96), (32, 32))),scala_tranform),
        ]
        self.ImagemParaDireita = [
            pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((0 * 32, 64), (32, 32))), scala_tranform),
            pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((1 * 32, 64), (32, 32))), scala_tranform)
        ]
        self.ImagemParaEsquerda = [
            pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((0 * 32, 96), (32, 32))), scala_tranform),
            pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((1 * 32, 96), (32, 32))), scala_tranform)
        ]


        self.index_lista = 0
        self.image = self.imagens[self.index_lista]

        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)


    def update(self):
        velocidade_animation = 0.2
        if self.index_lista >= len(self.imagens) - 1:
            self.index_lista = 0
        else:
            self.index_lista += velocidade_animation

        if self.animation == "direita":
            self.image = self.ImagemParaDireita[int(self.index_lista)]
        elif self.animation == "esquerda":
            self.image = self.ImagemParaEsquerda[int(self.index_lista)]
        elif self.animation == "tiro_direita":
            self.image = self.tiroDireita[int(self.index_lista)]
        elif self.animation == "tiro_esquerda":
            self.image = self.tiroEsquerda[int(self.index_lista)]
        else:
            self.image = self.imagens[int(self.index_lista)]
        

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.animation = "direita"
            if self.rect.x < pygame.display.get_surface().get_width():
                self.rect.x += 10
        elif keys[pygame.K_LEFT]:
            self.animation = "esquerda"
            if self.rect.x > 0:
                self.rect.x -= 10
        elif keys[pygame.K_UP]:
            if self.rect.y > pygame.display.get_surface().get_height() - 100:
                self.rect.y -= 10
            self.animation = "parado"
            # self.animation = "tiro_direita"
        elif keys[pygame.K_DOWN]:
            if self.rect.centery < pygame.display.get_surface().get_height():
                self.rect.y += 10
            self.animation = "parado"
            # self.animation = "tiro_esquerda"
        # elif keys[pygame.K_SPACE]:
        #     if self.animation == "direita":
        #         self.animation = "tiro_direita"
        #         tiro = Tiro("direita",self.inimigos)
        #         self.allSprites_group.add(tiro)
        #         tiro.rect.center = self.rect.center
        #     elif self.animation == "esquerda":
        #         self.animation = "tiro_esquerda"
        #         tiro = Tiro("esquerda",self.inimigos)
        #         self.allSprites_group.add(tiro)
        #         tiro.rect.center = self.rect.center
        # else:
        #     self.animation = "parado"



