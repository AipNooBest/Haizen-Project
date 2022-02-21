import pygame

from objects.glob import screen, groups


class Button(pygame.sprite.Sprite):
    def __init__(self, text, font, size, color):
        pygame.sprite.Sprite.__init__(self)
        self.text = _text_format(text, font, size, color)
        self.rect = self.text.get_rect()
        self.add(groups["all_sprites"])

    def change_text(self, text, font, size, color):
        self.text = _text_format(text, font, size, color)
        self.rect = self.text.get_rect()


selected = 0


def init():

    font = pygame.font.SysFont('EoSD', 35)
    text = font.render("Начать", True, "white")


def _text_format(text, font, size, color):
    new_font = pygame.font.SysFont(font, size)
    new_text = new_font.render(text, True, color)
    return new_text


def handle(event):
    screen.fill("black")
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            pass
        if event.key == pygame.K_UP:
            pass
        if event.key == pygame.K_RETURN:
            pass
