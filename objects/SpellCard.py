import pygame

from math import sin, cos, radians
from objects import glob
from objects.Bullet import Bullet


class SpellCard:
    def __init__(self, speed, angle, radius, caster=None, target=None):
        self.speed = speed
        self.angle = angle
        self.radius = radius
        if caster is not None:
            self.caster_x, self.caster_y = caster.rect.centerx, caster.rect.centery
        if target is not None:
            self.target_x, self.target_y = target.rect.centerx, target.rect.centery
        self.attack = None

    def set_attack(self, attack):
        self.attack = attack

    def set_caster(self, caster=None, coords=None):
        if coords is not None:
            self.caster_x, self.caster_y = coords
        if caster is not None:
            self.caster_x, self.caster_y = caster.rect.centerx, caster.rect.centery

    def set_target(self, target=None, coords=None):
        if coords is not None:
            self.caster_x, self.caster_y = coords
        if target is not None:
            self.caster_x, self.caster_y = target.rect.centerx, target.rect.centery


card = SpellCard(0, 0, 0)


def start(boss, spell):
    global card
    if spell == 1:
        card = SpellCard(8, 0, 0, boss)
        boss.HP = boss.max_HP = 180

        def attack():
            card.angle += 0.03
            card.angle %= 360
            for i in range(8):
                glob.Groups.enemy_bullets.add(
                    Bullet("pellet", card.caster_x, card.caster_y,
                           card.speed * cos(radians(sin(card.angle) * 900 + i * 45)),
                           card.speed * sin(radians(sin(card.angle) * 900 + i * 45))))
        card.set_attack(attack)
        pygame.time.set_timer(glob.Events.ENEMY_RELOAD, 50)

    if spell == 2:
        card = SpellCard(-9, 0, 120, boss)
        boss.HP = boss.max_HP = 240

        def attack():
            card.angle = card.angle + 12 % 360
            for i in range(12):
                glob.Groups.enemy_bullets.add(
                    Bullet("pellet", card.caster_x + cos(radians(i * 30 + card.angle)) * card.radius,
                           card.caster_y + sin(radians(i * 30 + card.angle)) * card.radius,
                           card.speed * cos(radians(i * 30 + 72)), card.speed * sin(radians(i * 30 + 72))))
        card.set_attack(attack)
        pygame.time.set_timer(glob.Events.ENEMY_RELOAD, 120)

    if spell == 3:
        # Заготовка третьей спелл-карты
        pass

    if spell == 4:
        card = SpellCard(8, 0, 0, boss)
        boss.HP = boss.max_HP = 180

        def attack():
            card.angle += 0.03
            card.angle %= 360
            for i in range(6):
                glob.Groups.enemy_bullets.add(
                    Bullet("pellet", card.caster_x, card.caster_y,
                           card.speed * cos(radians(sin(card.angle) * 900 + i * 60)),
                           card.speed * sin(radians(sin(card.angle) * 900 + i * 60))))

        card.set_attack(attack)
        pygame.time.set_timer(glob.Events.ENEMY_RELOAD, 100)

    if spell == 5:
        card = SpellCard(-9, 0, 120, boss)
        boss.HP = boss.max_HP = 240

        def attack():
            card.angle = card.angle + 12 % 360
            for i in range(8):
                glob.Groups.enemy_bullets.add(
                    Bullet("pellet", card.caster_x + cos(radians(i * 40 + card.angle)) * card.radius,
                           card.caster_y + sin(radians(i * 40 + card.angle)) * card.radius,
                           card.speed * cos(radians(i * 40 + 72)), card.speed * sin(radians(i * 40 + 72))))

        card.set_attack(attack)
        pygame.time.set_timer(glob.Events.ENEMY_RELOAD, 200)


def loop():
    card.attack()


def stop():
    global card
    pygame.time.set_timer(glob.Events.ENEMY_RELOAD, 0)
    card = SpellCard(0, 0, 0)
