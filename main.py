import pygame
import constants.playscreen
import constants.startscreen
import objects.glob

from constants.window import *
from constants.game_states import *

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
        if objects.glob.game_state == GameStates.MAIN_MENU:
            constants.startscreen.handle(event)
        elif objects.glob.game_state == GameStates.PLAYING or GameStates.PAUSED:
            constants.playscreen.handle(event)

    if objects.glob.game_state is not GameStates.PAUSED:
        objects.glob.groups["all_sprites"].update()
    objects.glob.groups["all_sprites"].draw(objects.glob.screen)
    pygame.display.flip()

pygame.quit()
