import pygame
import enum
import UI.handlers.main_menu

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
    BOMB_ATTACK = pygame.USEREVENT + 6
    BOMB_RELOAD = pygame.USEREVENT + 7


class GameStates(enum.IntEnum):
    MAIN_MENU = 0
    EXIT = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4
    WIN = 5


class Difficulty(enum.IntEnum):
    NORMAL = 0
    HARD = 1


class Settings:
    lives = 3
    bombs = 3
    bomb_type = 0
    difficulty = Difficulty.NORMAL


class Variables:
    screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)
    game_state = GameStates.MAIN_MENU
    current_screen = UI.handlers.main_menu.MainMenu()
    top_score = 0
