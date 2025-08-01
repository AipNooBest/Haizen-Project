import pygame

from objects import Global


class Text(pygame.sprite.Sprite):
    def __init__(self, text, font, color, position, alignment):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self._font = font
        self._color = color
        self.surface = font.render(text, False, color)
        self.rect = self.surface.get_rect()
        self.image = self.surface.subsurface(self.rect)
        self.alignment = self._align(position, alignment)
        self.add(Global.Groups.all_sprites)

    def change_text(self, text=None, font=None, color=None):
        if text is None: text = self.text
        if font is None: font = self._font
        if color is None: color = self._color
        old_position = (self.rect.x, self.rect.y)
        self.text = text
        self.surface = font.render(text, False, color)
        self.rect = self.surface.get_rect()
        self.image = self.surface.subsurface(self.rect)
        self.alignment = self._align(old_position, self.alignment)

    def _align(self, position, alignment):
        if alignment == 'left':
            self.rect.x, self.rect.y = position
        elif alignment == 'center':
            self.rect.centerx, self.rect.centery = position
        elif alignment == 'right':
            self.rect.topright = position
        else:
            raise AttributeError("Некорректное значение alignment")
        return alignment
