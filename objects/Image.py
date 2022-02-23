import os
import pygame

from objects.glob import groups


class Image(pygame.sprite.Sprite):
    def __init__(self, path, position, alignment, scale=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(path)).convert_alpha()

        if scale is not None:
            self.image = pygame.transform.scale(self.image, scale)
        else:
            self.rect = self.image.get_rect()

        if alignment == 'left':
            self.rect.x, self.rect.y = position
        elif alignment == 'center':
            self.rect.centerx, self.rect.centery = position
        elif alignment == 'right':
            self.rect.topright = position
        else:
            raise AttributeError("Некорректное значение alignment")

        self.add(groups["all_sprites"])
