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
        if self.rect.top < FRAME_TOP or self.rect.left < FRAME_LEFT or self.rect.right > FRAME_RIGHT or self.rect.bottom > FRAME_BOTTOM:
            self.kill()
