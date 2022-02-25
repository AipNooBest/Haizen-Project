import pygame
import objects.SpellCard
import handlers.playscreen

from constants.window import *
from objects import glob


class Enemy(pygame.sprite.Sprite):
    def __init__(self, hp):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = (FRAME_LEFT + FRAME_RIGHT) / 2
        self.rect.centery = 160
        self.angle = 0
        self._layer = 3
        self.HP = hp
        self.max_HP = hp
        self.add(glob.Groups.all_sprites)
        self.add(glob.Groups.mobs)

    def update(self):
        hits = pygame.sprite.spritecollide(self, glob.Groups.player_bullets, True)
        for _ in hits:
            self.HP -= 1
            handlers.playscreen.update_sprites("ENEMY_HP", "set", self.HP)

        if self.HP <= 0:
            objects.SpellCard.stop()
            self.kill()

    def attack(self):
        objects.SpellCard.start(self, 1)
