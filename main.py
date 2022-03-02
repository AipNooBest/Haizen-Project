import os
import pygame
import handlers.playscreen
import handlers.main_menu

from objects import glob
from constants.window import *
from constants.game_states import *

# Инициализация
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Haizen Project")
pygame.display.set_icon(pygame.image.load(os.path.join("assets/icon.ico")).convert_alpha())
clock = pygame.time.Clock()
handlers.main_menu.init()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if glob.game_state == GameStates.MAIN_MENU:
            handlers.main_menu.handle(event)
        elif glob.game_state == GameStates.PLAYING or GameStates.PAUSED:
            handlers.playscreen.handle(event)

    if glob.game_state is not GameStates.PAUSED:
        glob.Groups.all_sprites.update()
    glob.Groups.all_sprites.draw(glob.screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
