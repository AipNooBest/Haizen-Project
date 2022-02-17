import pygame

from constants.window import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, startX, startY, speedX, speedY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((6, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = startX
        self.rect.y = startY
        self.speedx = speedX
        self.speedy = speedY

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20 or self.rect.bottom < -10:
            self.kill()
