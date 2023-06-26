import pygame


# Transformar numa função


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
