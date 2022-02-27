import pygame

from objects import glob


class Text(pygame.sprite.Sprite):
    def __init__(self, text, font, size, color, position, alignment):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self._font = font
        self._size = size
        self._color = color
        self.surface = _text_format(text, font, size, color)
        self.rect = self.surface.get_rect()
        self.image = self.surface.subsurface(self.rect)
        self.alignment = self._align(position, alignment)
        self.add(glob.Groups.all_sprites)

    def change_text(self, text=None, font=None, size=None, color=None):
        if text is None: text = self.text
        if font is None: font = self._font
        if size is None: size = self._size
        if color is None: color = self._color
        old_position = (self.rect.x, self.rect.y)
        self.text = text
        self.surface = _text_format(text, font, size, color)
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


def _text_format(text, font, size, color):
    new_font = pygame.font.SysFont(font, size)
    new_text = new_font.render(text, False, color)
    return new_text
