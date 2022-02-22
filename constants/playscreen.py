import pygame
import objects.SpellCard

from objects.glob import groups, events, screen
from constants.window import *
from objects.Enemy import Enemy
from objects.Player import Player

# Глобальные переменные
player = None
enemy = None


class PlayField(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill('darkgreen')
        self.rect = self.image.get_rect()
        self._layer = 0
        self.rect.x = x
        self.rect.y = y
        self.add(groups["all_sprites"])
        self.add(groups["border"])


def init():
    global player, enemy
    PlayField(FRAME_LEFT, FRAME_TOP, FRAME_RIGHT-FRAME_LEFT, FRAME_BOTTOM-FRAME_TOP)
    pygame.time.set_timer(events["enemy_attack_event"], 1000, 1)
    player = Player()
    enemy = Enemy(80)


def handle(event):
    global player, enemy
    if player is None or enemy is None:
        return
    if event.type == pygame.USEREVENT:
        player.reloaded = True
        pygame.time.set_timer(events["reloaded_event"], 0)
    if event.type == pygame.USEREVENT + 1:
        enemy.attack()
    if event.type == pygame.USEREVENT + 2:
        objects.SpellCard.loop()

    screen.fill(BLACK)
