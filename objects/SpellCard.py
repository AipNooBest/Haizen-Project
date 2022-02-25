import pygame

from math import sin, cos, radians
from objects import glob
from objects.Bullet import Bullet


class SpellCard:
    def __init__(self, speed, angle, relative_x, relative_y, func):
        self.speed = speed
        self.angle = angle
        self.relative_x = relative_x
        self.relative_y = relative_y
        self.attack = func


current_atk = SpellCard(0, 0, 0, 0, None)


def start(enemy, spell):
    global current_atk
    attack = None
    if spell == 1:
        def attack():
            current_atk.angle += 0.03
            current_atk.angle %= 360
            for i in range(8):
                glob.Groups.enemy_bullets.add(
                    Bullet("pellet", current_atk.relative_x, current_atk.relative_y,
                           current_atk.speed * cos(radians(sin(current_atk.angle)*900 + i * 45)),
                           current_atk.speed * sin(radians(sin(current_atk.angle)*900 + i * 45))))
    current_atk = SpellCard(8, 0, enemy.rect.centerx, enemy.rect.centery, attack)
    pygame.time.set_timer(glob.Events.ENEMY_RELOAD, 50)


def loop():
    current_atk.attack()


def stop():
    global current_atk
    pygame.time.set_timer(glob.Events.ENEMY_RELOAD, 0)
    current_atk = SpellCard(0, 0, 0, 0, None)
