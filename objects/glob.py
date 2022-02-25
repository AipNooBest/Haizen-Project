import pygame
import enum

from constants.window import WIDTH, HEIGHT


class Groups(enum.auto):
    all_sprites = pygame.sprite.LayeredUpdates()
    mobs = pygame.sprite.LayeredUpdates()
    player_bullets = pygame.sprite.LayeredUpdates()
    enemy_bullets = pygame.sprite.LayeredUpdates()
    border = pygame.sprite.Group()


class Events(enum.IntEnum):
    PLAYER_RELOAD = pygame.USEREVENT
    ENEMY_ATTACK = pygame.USEREVENT + 1
    ENEMY_RELOAD = pygame.USEREVENT + 2
    MOVING_END = pygame.USEREVENT + 3
    GOD_MODE_END = pygame.USEREVENT + 4
    FLASHING = pygame.USEREVENT + 5


screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_state = 0
