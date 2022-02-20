import pygame

from math import sin, cos, pi, radians
from objects.Bullet import Bullet
from objects.glob import groups, events


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

            current_atk.angle += 44
            current_atk.angle %= 360
            for i in range(6):
                groups["enemy_bullets"].add(
                    Bullet("pellet", current_atk.relative_x, current_atk.relative_y,
                           current_atk.speed * cos(radians(current_atk.angle + i * 60)),
                           current_atk.speed * sin(radians(current_atk.angle + i * 60))))
    current_atk = SpellCard(10, 0, enemy.rect.centerx, enemy.rect.centery, attack)
    pygame.time.set_timer(events["enemy_reloaded_event"], 60)


def loop():
    current_atk.attack()


def stop():
    global current_atk
    pygame.time.set_timer(events["enemy_reloaded_event"], 0)
    current_atk = SpellCard(0, 0, 0, 0, None)
