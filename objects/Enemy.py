import pygame

from math import sin, cos, pi
from constants.window import *
from objects.Bullet import Bullet
from objects.glob import groups, events


class Enemy(pygame.sprite.Sprite):
    def __init__(self, hp):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = FRAME_LEFT + FRAME_RIGHT / 2
        self.rect.centery = 80
        self.angle = 0
        self._layer = 3
        self.HP = hp

    def update(self):
        hits = pygame.sprite.spritecollide(self, groups["player_bullets"], True)
        for _ in hits:
            self.HP -= 1
        if self.HP <= 0:
            self.kill()

    def attack(self):
        if self.HP <= 0:
            return
        speed = 10
        groups["enemy_bullets"].add(
            Bullet("pellet", self.rect.centerx, self.rect.centery, speed * cos(self.angle * pi / 180),
                   speed * sin(self.angle * pi / 180)))
        groups["enemy_bullets"].add(
            Bullet("pellet", self.rect.centerx, self.rect.centery, speed * cos((self.angle + 90) * pi / 180),
                   speed * sin((self.angle + 90) * pi / 180)))
        groups["enemy_bullets"].add(
            Bullet("pellet", self.rect.centerx, self.rect.centery, speed * cos((self.angle + 180) * pi / 180),
                   speed * sin((self.angle + 180) * pi / 180)))
        groups["enemy_bullets"].add(
            Bullet("pellet", self.rect.centerx, self.rect.centery, speed * cos((self.angle + 270) * pi / 180),
                   speed * sin((self.angle + 270) * pi / 180)))
        self.angle += 23
        pygame.time.set_timer(events["enemy_attack_event"], 50)
