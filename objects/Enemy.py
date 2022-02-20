import pygame
from constants.window import *
from objects.glob import groups


class Enemy(pygame.sprite.Sprite):
    def __init__(self, hp):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = 80
        self._layer = 3
        self.HP = hp

    def update(self):
        hit = pygame.sprite.spritecollideany(self, groups["bullets"])
        if hit:
            hit.kill()
            self.HP -= 1
        if self.HP <= 0:
            self.kill()
