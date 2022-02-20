import pygame

from objects.glob import groups, events
from constants.window import *


class PlayField(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill('darkgreen')
        self.rect = self.image.get_rect()
        self._layer = 0
        self.rect.x = x
        self.rect.y = y
        self.add(groups["all_sprites"])
        self.add(groups["border"])


def init():
    PlayField(FRAME_LEFT, FRAME_TOP, FRAME_RIGHT-FRAME_LEFT, FRAME_BOTTOM-FRAME_TOP)
    pygame.time.set_timer(events["enemy_attack_event"], 1000, 1)
