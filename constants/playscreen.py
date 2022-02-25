import pygame
import objects.SpellCard
import objects.glob

from constants.window import *
from constants.game_states import *
from objects.Enemy import Enemy
from objects.Player import Player
from objects.Text import Text
from objects.Image import Image
from objects.Bar import Bar

# Глобальные переменные
player: Player
enemy: Enemy
RESOURCES_X = FRAME_RIGHT + 40
RESOURCES_Y = FRAME_BOTTOM * 3 / 4
HP_sprites = []
Bomb_sprites = []
health_bar: Bar
paused = False


class PlayField(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill('darkgreen')
        self.rect = self.image.get_rect()
        self._layer = 0
        self.rect.x = x
        self.rect.y = y
        self.add(objects.glob.groups["all_sprites"])
        self.add(objects.glob.groups["border"])


def init():
    global player, enemy, health_bar
    PlayField(FRAME_LEFT, FRAME_TOP, FRAME_RIGHT-FRAME_LEFT, FRAME_BOTTOM-FRAME_TOP)
    pygame.time.set_timer(objects.glob.events["enemy_attack_event"], 1000, 1)
    pygame.time.set_timer(objects.glob.events["reloaded_event"], 400)
    player = Player()
    enemy = Enemy(120)
    Text("ЖИЗНИ:", "Segoe Script", 30, "white", (RESOURCES_X, RESOURCES_Y - 50), "left")
    for i in range(player.HP):
        HP_sprites.append(Image("assets/health-point.png", (RESOURCES_X + 35*i, RESOURCES_Y), "left"))
    Text("БОМБЫ:", "Segoe Script", 30, "white", (RESOURCES_X, RESOURCES_Y + 50), "left")
    for i in range(player.HP):   # TODO: Позже заменить на бомбы
        Bomb_sprites.append(Image("assets/bomb.png", (RESOURCES_X + 35*i, RESOURCES_Y + 100), "left"))

    health_bar = Bar(enemy.HP, enemy.max_HP)


def handle(event):
    global player, enemy, paused
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        paused = not paused
        objects.glob.game_state = GameStates.PAUSED if paused else GameStates.PLAYING
    if player is None or enemy is None or paused:
        return
    if event.type == pygame.USEREVENT:
        player.reloaded = True
        pygame.time.set_timer(objects.glob.events["reloaded_event"], 0)
    elif event.type == pygame.USEREVENT + 1:
        enemy.attack()
    elif event.type == pygame.USEREVENT + 2:
        objects.SpellCard.loop()
    elif event.type == pygame.USEREVENT + 3:
        player.movable = True
        player.speedY = 0
    elif event.type == pygame.USEREVENT + 4:
        pygame.time.set_timer(objects.glob.events["flashing"], 0, 0)
        pygame.time.set_timer(objects.glob.events["invincibility_end"], 0, 0)
        player.invincible = False
        player.visible = True
        player.image.set_alpha(255)
    elif event.type == pygame.USEREVENT + 5:
        if player.visible:
            player.image.set_alpha(0)
            player.visible = False
        else:
            player.image.set_alpha(255)
            player.visible = True

    objects.glob.screen.fill(BLACK)


def update_sprites(sprite_type, action, value=None):
    if sprite_type == "PLAYER_HP":
        if action == "append":
            HP_sprites.append(
                Image("assets/health-point.png", (RESOURCES_X + 35*len(HP_sprites), RESOURCES_Y), "left"))
        elif action == "reduce":
            HP_sprites.pop().kill()
    elif sprite_type == "PLAYER_BOMB":
        if action == "append":
            Bomb_sprites.append(
                Image("assets/health-point.png", (RESOURCES_X + 35 * len(HP_sprites), RESOURCES_Y), "left"))
        elif action == "reduce":
            Bomb_sprites.pop().kill()
    elif sprite_type == "ENEMY_HP":
        if action == "set":
            health_bar.set_value(value)
