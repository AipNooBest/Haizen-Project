import pygame
import constants.playscreen
import constants.startscreen
import objects.glob

from constants.window import *

# Инициализация
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Haizen Project")
clock = pygame.time.Clock()
constants.startscreen.init()


# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if objects.glob.game_state == 0:
            constants.startscreen.handle(event)
        elif objects.glob.game_state == 1:
            constants.playscreen.handle(event)

    objects.glob.groups["all_sprites"].update()
    objects.glob.groups["all_sprites"].draw(objects.glob.screen)
    pygame.display.flip()

pygame.quit()
