import os
import pygame

from objects.Global import GameStates, Variables, Groups
from constants.window import *

# Инициализация
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Haizen Project")
pygame.display.set_icon(pygame.image.load(os.path.join("assets/icon.ico")).convert_alpha())
clock = pygame.time.Clock()


# Game loop
while Variables.game_state != GameStates.QUIT:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Variables.game_state = GameStates.QUIT
            break
        Variables.current_screen.handle(event)
    if Variables.game_state is not GameStates.PAUSED:
        Groups.all_sprites.update()
    Groups.all_sprites.draw(Variables.screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
