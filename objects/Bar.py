import pygame
import objects.glob

from constants.window import *


class Bar(pygame.sprite.Sprite):
    def __init__(self, value, max_value=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((FRAME_RIGHT - FRAME_LEFT - 40, 10))
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = FRAME_LEFT + 20, FRAME_TOP + 10
        self.max_value = max_value if max_value is not None else value
        self.rect.width = self.image.get_width() * value / self.max_value
        self.add(objects.glob.groups["all_sprites"])

    def set_value(self, value):
        value %= self.max_value
        self.image = pygame.transform.scale(self.image, (self.rect.width * value / self.max_value, 10))
