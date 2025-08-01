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

# Глобальные переменные
player: Player
enemy: Enemy
RESOURCES_X = FRAME_RIGHT + 40
RESOURCES_Y = FRAME_BOTTOM * 3 / 4
HP_sprites = []
Bomb_sprites = []
health_bar: Bar
paused = False
score_text: Text


class PlayField(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.image.blit(pygame.image.load(os.path.join("assets/background.png")).convert_alpha(), self.rect)
        self._layer = 0
        self.rect.x = x
        self.rect.y = y
        self.add(Global.Groups.all_sprites)
        self.add(Global.Groups.border)


def init():
    global player, enemy, health_bar, score_text
    PlayField(FRAME_LEFT, FRAME_TOP, FRAME_RIGHT-FRAME_LEFT, FRAME_BOTTOM-FRAME_TOP)
    pygame.time.set_timer(Global.Events.ENEMY_ATTACK, 1000, 1)
    pygame.time.set_timer(Global.Events.PLAYER_RELOAD, 400)
    player = Player()
    if Global.difficulty == Global.Difficulty.NORMAL:
        enemy = Enemy([5, 4])
    if Global.difficulty == Global.Difficulty.HARD:
        enemy = Enemy([2, 1])
    Text("ЖИЗНИ:", "Segoe Script", 30, "white", (RESOURCES_X, RESOURCES_Y - 50), "left")
    for i in range(player.lives):
        HP_sprites.append(Image("assets/health-point.png", (RESOURCES_X + 35*i, RESOURCES_Y), "left"))
    Text("БОМБЫ:", "Segoe Script", 30, "white", (RESOURCES_X, RESOURCES_Y + 50), "left")
    for i in range(player.bombs):
        Bomb_sprites.append(Image("assets/bomb.png", (RESOURCES_X + 35*i, RESOURCES_Y + 100), "left"))
    Text("СЧЁТ", "Segoe Script", 30, "white", (RESOURCES_X + 125, RESOURCES_Y - 300), "center")
    score_text = Text("{:08}".format(Global.score), "Segoe Script", 32, "white", (RESOURCES_X + 40, RESOURCES_Y - 270), "left")
    health_bar = Bar(1, 1)
    music = pygame.mixer.Sound('assets/A Shower of Strange Occurrences.wav')
    # music.play(1)
    music.set_volume(0.3)


def handle(event):
    global player, enemy, paused, health_bar
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        paused = not paused
        Global.game_state = GameStates.PAUSED if paused else GameStates.PLAYING
    if player is None or enemy is None or paused:
        return
    if event.type == Global.Events.PLAYER_RELOAD:
        player.reloaded = True
        pygame.time.set_timer(Global.Events.PLAYER_RELOAD, 0)
    elif event.type == Global.Events.ENEMY_ATTACK:
        enemy.attack(enemy.atk_sequence[len(enemy.atk_sequence) - 1])
        health_bar.kill()
        health_bar = Bar(enemy.HP, enemy.max_HP)
    elif event.type == Global.Events.ENEMY_RELOAD:
        objects.SpellCard.loop()
    elif event.type == Global.Events.MOVING_END:
        player.movable = True
        player.speedY = 0
    elif event.type == Global.Events.GOD_MODE_END:
        pygame.time.set_timer(Global.Events.FLASHING, 0, 0)
        pygame.time.set_timer(Global.Events.GOD_MODE_END, 0, 0)
        player.god_mode = False
        player.visible = True
        player.image.set_alpha(255)
    elif event.type == Global.Events.FLASHING:
        if player.visible:
            player.image.set_alpha(0)
            player.visible = False
        else:
            player.image.set_alpha(255)
            player.visible = True
    elif event.type == Global.Events.BOMB_ATTACK:
        player.handle_bombs(player, enemy)
    elif event.type == Global.Events.BOMB_RELOAD:
        player.using_bomb = False
        pygame.time.set_timer(Global.Events.BOMB_ATTACK, 0, 0)

    Global.screen.fill(BLACK)


def update_sprites(sprite_type, action, value=None):
    if sprite_type == "PLAYER_HP":
        if action == "append":
            HP_sprites.append(
                Image("assets/health-point.png", (RESOURCES_X + 35*len(HP_sprites), RESOURCES_Y), "left"))
        elif action == "reduce":
            HP_sprites.pop().kill() if len(HP_sprites) > 0 else None
    elif sprite_type == "PLAYER_BOMB":
        if action == "append":
            Bomb_sprites.append(
                Image("assets/health-point.png", (RESOURCES_X + 35 * len(HP_sprites), RESOURCES_Y), "left"))
        elif action == "reduce":
            Bomb_sprites.pop().kill() if len(Bomb_sprites) > 0 else None
    elif sprite_type == "ENEMY_HP":
        if action == "set":
            if value == -1: return
            health_bar.set_value(value)
    elif sprite_type == "SCORE":
        if action == "set":
            score_text.change_text(text="{:08.0f}".format(Global.score))
