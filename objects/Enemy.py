import os
import pygame
import objects.SpellCard
import handlers.playscreen

from constants.window import *
from objects import Global
from typing import List


class Enemy(pygame.sprite.Sprite):
    def __init__(self, atk_sequence: List[int]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("assets/enemy.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = (FRAME_LEFT + FRAME_RIGHT) / 2
        self.rect.centery = 160
        self.angle = 0
        self._layer = 3
        self.HP = None
        self.max_HP = None
        self.atk_sequence = atk_sequence
        self.add(Global.Groups.all_sprites)
        self.add(Global.Groups.mobs)

    def update(self):
        hits = pygame.sprite.spritecollide(self, Global.Groups.player_bullets, True)
        if self.HP is None: return
        for _ in hits:
            self.HP -= 1
            Global.score = Global.score + 100 * ((0.5 * 0.98 ** Global.lives) + (0.5 * 0.98 ** Global.bombs)) * (Global.difficulty + 1)
            handlers.playscreen.update_sprites("ENEMY_HP", "set", max(self.HP, 0))
            handlers.playscreen.update_sprites("SCORE", "set", Global.score)

        if self.HP <= 0:
            objects.SpellCard.stop()
            self.atk_sequence.pop()
            if len(self.atk_sequence) == 0:
                self.kill()
            else:
                pygame.time.set_timer(Global.Events.ENEMY_ATTACK, 1000, 1)
                pygame.time.set_timer(Global.Events.ENEMY_RELOAD, 0, 0)
                self.HP = None

    def attack(self, attack_type):
        objects.SpellCard.start(self, attack_type)
