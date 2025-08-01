import pygame

from UI.elements.Text import Text


class Button:
    def __init__(self, text, x, y, callback, font=pygame.font.SysFont("Segoe Script", 32), color="white",
                 alignment="left"):
        self.text = text
        self.callback = callback
        self.selected = False
        self.text_object = Text(text, font, color, (x, y), alignment)
        self.rect = pygame.Rect(x, y)

    def select(self):
        self.selected = True
        self.text_object.change_text(color="white")
        self.rect.x -= 20

    def deselect(self):
        self.selected = False
        self.text_object.change_text(color="grey")
        self.rect.x += 20