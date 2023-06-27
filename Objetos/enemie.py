import pygame
import random


class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        tipo = random.choice(["orc", "zombie"])
        inimigo_imagem = pygame.image.load("Assets/Primeira fase/Pixel_Enemy_Platformer/Skeleton_Big.png").convert_alpha()
        
        self.imagens = []
        
        if tipo == "orc":
            inimigo_imagem = pygame.image.load("Assets/Primeira fase/Pixel_Enemy_Platformer/Orc_Big.png").convert_alpha()
        elif tipo == "zombie":
            inimigo_imagem = pygame.image.load("Assets/Primeira fase/Pixel_Enemy_Platformer/Zombie_Big.png").convert_alpha()
        
        for i in range(3):
            img = inimigo_imagem.subsurface(pygame.Rect((0, i * 32), (64, 32)))
            img = pygame.transform.scale(img, scala_tranform)
            self.imagens.append(img)        

        self.index_lista = 0
        self.image = self.imagens[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)

    def update(self):
        if self.index_lista >= len(self.imagens) - 1:
            self.index_lista = 0    
        else:
            self.index_lista += 0.25

        self.image = self.imagens[int(self.index_lista)]
