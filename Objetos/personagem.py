import pygame

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.animation = "parado" # -> Mudar sprit

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
        self.imagens = [
            pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((1 * 32, 0), (32, 32))), scala_tranform),
            pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((2 * 32, 0), (32, 32))), scala_tranform)
        ]
        self.ImagemParaDireita = [
            pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((1 * 32, 64), (32, 32))), scala_tranform),
            pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((2 * 32, 64), (32, 32))), scala_tranform)
        ]
        self.ImagemParaEsquerda = [
            pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((1 * 32, 96), (32, 32))), scala_tranform),
            pygame.transform.scale(personagem_imagem.subsurface(pygame.Rect((2 * 32, 96), (32, 32))), scala_tranform)
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
