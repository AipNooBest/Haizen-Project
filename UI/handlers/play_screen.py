import os
import pygame
import objects.SpellCard

from constants.window import *
from objects import Global
from objects.Enemy import Enemy
from objects.Player import Player
from UI.elements.Text import Text
from UI.elements.Image import Image
from UI.elements.Bar import Bar

RESOURCES_X = FRAME_RIGHT + 40
RESOURCES_Y = FRAME_BOTTOM * 3 / 4


class PlayScreen:
    def __init__(self):
        self.player = Player()
        self.enemies = []
        self.health_bar: Bar
        self.score = 0
        self.HP_sprites = []
        self.Bomb_sprites = []
        self.score_text = pygame.sprite.Sprite()
        self.field = pygame.sprite.Sprite()

        self._init_field()

    def _init_field(self):
        self.field.image = pygame.Surface((FRAME_RIGHT-FRAME_LEFT, FRAME_BOTTOM-FRAME_TOP))
        self.field.rect = self.field.image.get_rect()
        self.field.rect.x, self.field.rect.y = FRAME_LEFT, FRAME_TOP
        self.field.image.blit(pygame.image.load(os.path.join("assets/background.png")).convert_alpha(), field.rect)
        self.field._layer = 0
        Global.Groups.all_sprites.add(self.field)
        Global.Groups.border.add(self.field)

    def _init_ui(self):
        font = pygame.font.SysFont("Segoe Script", 30)

        self.score_text = Text(str(self.score), font, "white", (RESOURCES_X + 125, RESOURCES_Y - 250), "center")
        Text("ЖИЗНИ:", font, "white", (RESOURCES_X, RESOURCES_Y - 50), "left")
        for i in range(self.player.lives):
            self.HP_sprites.append(Image("assets/health-point.png", (RESOURCES_X + 35*i, RESOURCES_Y), "left"))
        Text("БОМБЫ:", font, "white", (RESOURCES_X, RESOURCES_Y + 50), "left")
        for i in range(self.player.bombs):
            self.Bomb_sprites.append(Image("assets/bomb.png", (RESOURCES_X + 35*i, RESOURCES_Y + 100), "left"))
        Text("СЧЁТ", font, "white", (RESOURCES_X + 125, RESOURCES_Y - 300), "center")

    def _init_misc(self):
        pygame.time.set_timer(Global.Events.ENEMY_ATTACK, 1000, 1)
        pygame.time.set_timer(Global.Events.PLAYER_RELOAD, 400)

    def handle(self, event):
        if event.type == Global.Events.PLAYER_RELOAD:
            self.player.reloaded = True
            pygame.time.set_timer(Global.Events.PLAYER_RELOAD, 0)
        elif event.type == Global.Events.ENEMY_ATTACK:
            self.enemies[0].attack()
            pygame.time.set_timer(Global.Events.ENEMY_ATTACK, 0)

    def update(self):
        self.update_ui()

    def update_ui(self):
        pass