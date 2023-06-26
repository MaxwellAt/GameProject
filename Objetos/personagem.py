import pygame

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
