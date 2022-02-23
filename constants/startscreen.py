import sys
import pygame

import constants.playscreen
import objects.glob
from constants.window import *


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
        self.add(objects.glob.groups["all_sprites"])

    def change_text(self, text, font, size, color):
        if text is None: text = self.text
        if font is None: font = self._font
        if size is None: size = self._size
        if color is None: color = self._color
        old_position = (self.rect.x, self.rect.y)
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


selected = 0
buttons = []
DEF_BUTTON_X = WIDTH - 90


def init():
    Text("Haizen Project", "EoSD", 35, "white", (WIDTH / 2, HEIGHT / 4), "center")
    buttons.append(Text("Start", "EoSD", 35, "grey", (DEF_BUTTON_X, HEIGHT / 2), "right"))
    buttons.append(Text("Quit", "EoSD", 35, "grey", (DEF_BUTTON_X, HEIGHT / 2 + 40), "right"))


def _text_format(text, font, size, color):
    new_font = pygame.font.SysFont(font, size)
    new_text = new_font.render(text, False, color)
    return new_text


def handle(event):
    global selected
    if objects.glob.game_state != 0: return
    objects.glob.screen.fill("black")
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            buttons[selected].rect.x = DEF_BUTTON_X
            buttons[selected].change_text(None, None, None, "grey")
            selected += 1
        if event.key == pygame.K_UP:
            buttons[selected].rect.x = DEF_BUTTON_X
            buttons[selected].change_text(None, None, None, "grey")
            selected -= 1
        if event.key == pygame.K_z:
            if selected == 0:
                unload()
                constants.playscreen.init()
                objects.glob.game_state = 1
                return
            else: sys.exit()

    selected %= len(buttons)
    buttons[selected].rect.x = DEF_BUTTON_X - 20
    buttons[selected].change_text(None, None, None, "white")


def unload():
    objects.glob.groups["all_sprites"].empty()
    buttons.clear()
