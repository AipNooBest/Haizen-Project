import pygame

from constants.window import *
from objects.glob import groups


class Bullet(pygame.sprite.Sprite):
    def __init__(self, type, startX, startY, speedX, speedY):
        pygame.sprite.Sprite.__init__(self)
        if type == "pin":
            self.image = pygame.Surface((6, 10))
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
        if type == "pellet":
            radius = 4
            self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(self.image, WHITE, (radius, radius), radius)
            self.rect = pygame.Rect(startX, startY, radius * 2, radius * 2)

        groups["bullets"].add(self)
        groups["all_sprites"].add(self)
        self._layer = 1
        self.rect.x = startX
        self.rect.y = startY
        self.speedx = speedX
        self.speedy = speedY

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top < FRAME_TOP or self.rect.left < FRAME_LEFT or self.rect.right > FRAME_RIGHT or self.rect.bottom > FRAME_BOTTOM:
            self.kill()
