import pygame
from constants.window import WIDTH, HEIGHT

groups = {
    "all_sprites": pygame.sprite.LayeredUpdates(),
    "mobs": pygame.sprite.LayeredUpdates(),
    "player_bullets": pygame.sprite.LayeredUpdates(),
    "enemy_bullets": pygame.sprite.LayeredUpdates(),
    "border": pygame.sprite.Group(),
}

events = {
    "reloaded_event": pygame.USEREVENT,
    "enemy_attack_event": pygame.USEREVENT + 1,
    "enemy_reloaded_event": pygame.USEREVENT + 2
}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_state = 0
