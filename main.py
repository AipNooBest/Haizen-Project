import pygame
import constants.playscreen
import constants.startscreen

from constants.window import *
from objects.glob import groups, screen

# Инициализация
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Haizen Project")
clock = pygame.time.Clock()
state = 1
constants.playscreen.init()


# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if state == 0:
            constants.startscreen.handle(event)
        elif state == 1:
            constants.playscreen.handle(event)

    groups["all_sprites"].update()
    groups["all_sprites"].draw(screen)
    pygame.display.flip()

pygame.quit()
