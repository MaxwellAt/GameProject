import pygame

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
        self.rect.center = (100, 40)

    def update(self):
        if self.index_lista >= len(self.imagens) - 1:
            self.index_lista = 0
        else:
            self.index_lista += 1
        self.image = self.imagens[self.index_lista]