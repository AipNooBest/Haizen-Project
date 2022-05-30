import os
import pygame

from constants.window import *
from objects import glob


class Bullet(pygame.sprite.Sprite):
    def __init__(self, type, startX, startY, speedX, speedY):
        pygame.sprite.Sprite.__init__(self)
        if type == "pin":
            self.image = pygame.image.load(os.path.join("assets/pin_bullet.png")).convert_alpha()
            self.rect = self.image.get_rect()
        if type == "pellet":
            radius = 4
            self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(self.image, WHITE, (radius, radius), radius)
            self.rect = pygame.Rect(startX, startY, radius * 2, radius * 2)

        glob.Groups.all_sprites.add(self)
        self._layer = 1
        self.rect.x = startX
        self.rect.y = startY
        self.position = pygame.math.Vector2(startX, startY)
        self.velocity = pygame.math.Vector2(speedX, speedY)

    def update(self):
        self.position += self.velocity
        self.rect.center = round(self.position[0]), round(self.position[1])
        if self.rect.top < FRAME_TOP or self.rect.left < FRAME_LEFT or self.rect.right > FRAME_RIGHT or self.rect.bottom > FRAME_BOTTOM:
            self.kill()
