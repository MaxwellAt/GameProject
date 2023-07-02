import pygame

# Transformar numa função

class Tiro(pygame.sprite.Sprite):
    def __init__(self,direcao,inimigos:list):
        pygame.sprite.Sprite.__init__(self)

        tiro_imagem = pygame.image.load("Assets/Primeira fase/Pixel_Enemy_Platformer/Bullet_Orc_B.png").convert_alpha()

        self.direction = direcao
        self.inimigos = inimigos


        self.image = pygame.transform.scale(tiro_imagem.subsurface(pygame.Rect((0, 16), (16, 16))), (16,16))
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)

        # Achar um bom som para o tiro
        # pygame.mixer.music.load("Assets/Music/bala.mp3")
        # pygame.mixer.music.play()
        # Codigo acima é do barulho sonoro do tiro quando é disparado.

    def update(self):
        # Ele tem que eliminar a sprit que ele colidiu
        if self.direction == "direita":
            self.rect.x +=10
        elif self.direction == "esquerda":
            self.rect.x -=10
        for inimigo in self.inimigos:
            if pygame.sprite.collide_rect(self,inimigo):
                inimigo.kill()
                self.kill()
                self.inimigos.remove(inimigo)
