import pygame
from objects.glob import groups


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        pygame.sprite.Sprite.__init__(self)
        if x1 == x2:
            self.add(groups["vertical_border"])
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        elif y1 == y2:
            self.add(groups["horizontal_border"])
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
        else:
            raise Exception("Некорректные значения границ!")
