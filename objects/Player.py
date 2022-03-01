import pygame
import handlers.playscreen

from math import sin, cos, radians
from constants.window import *
from objects import glob
from objects.Bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((23, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = (FRAME_LEFT + FRAME_RIGHT) / 2
        self.rect.centery = FRAME_BOTTOM - 40
        self.movable = True
        self.god_mode = False
        self.using_bomb = False
        self.visible = True
        self.lives = glob.lives
        self.bombs = glob.bombs
        self.bomb_type = _init_bomb(glob.bomb_type)
        self.speedX = 0
        self.speedY = 0
        self.reloaded = False
        self.reload_speed = 60
        self.add(glob.Groups.all_sprites)

    def update(self) -> None:
        if pygame.sprite.spritecollide(self, glob.Groups.enemy_bullets, True) and not self.god_mode:
            handlers.playscreen.update_sprites("PLAYER_HP", "reduce")
            self.lives -= 1
            self.respawn()
        if self.lives < 0:
            self.kill()
        if not self.movable:
            self.rect.x += self.speedX
            self.rect.y += self.speedY
            return
        if not self.visible and not self.god_mode:
            self.visible = True
            self.image.set_alpha(255)

        self.speedX = 0
        self.speedY = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedX = -6
        if keystate[pygame.K_RIGHT]:
            self.speedX = 6
        if keystate[pygame.K_UP]:
            self.speedY = -6
        if keystate[pygame.K_DOWN]:
            self.speedY = 6
        if keystate[pygame.K_LSHIFT]:
            self.speedX /= 2
            self.speedY /= 2
        if keystate[pygame.K_z]:
            self.shoot()
        if keystate[pygame.K_x] and not self.using_bomb and self.bombs > 0:
            self.use_bomb()
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.right > FRAME_RIGHT:
            self.rect.right = FRAME_RIGHT
        if self.rect.left < FRAME_LEFT:
            self.rect.left = FRAME_LEFT
        if self.rect.bottom > FRAME_BOTTOM:
            self.rect.bottom = FRAME_BOTTOM
        if self.rect.top < FRAME_TOP:
            self.rect.top = FRAME_TOP

    def shoot(self):
        if self.reloaded:
            self.reloaded = False
            speed = 20
            pygame.time.set_timer(glob.Events.PLAYER_RELOAD, self.reload_speed)
            glob.Groups.player_bullets.add(Bullet("pin", self.rect.centerx - 10, self.rect.y - 15, 0, -speed))
            glob.Groups.player_bullets.add(Bullet("pin", self.rect.centerx + 5, self.rect.y - 15, 0, -speed))

    def use_bomb(self):
        self.bombs -= 1
        handlers.playscreen.update_sprites("PLAYER_BOMB", "reduce")
        self.god_mode = True
        self.using_bomb = True
        glob.Groups.enemy_bullets.empty()
        pygame.time.set_timer(glob.Events.GOD_MODE_END, 3000, 0)
        pygame.time.set_timer(glob.Events.FLASHING, 100)
        pygame.time.set_timer(glob.Events.BOMB_RELOAD, 500, 1)
        pygame.time.set_timer(glob.Events.BOMB_ATTACK, 30)

    def handle_bombs(self, enemy):
        self.bomb_type.attack(enemy)

    def respawn(self):
        self.god_mode = True
        self.movable = False
        self.rect.centerx = (FRAME_LEFT + FRAME_RIGHT) / 2
        self.rect.centery = FRAME_BOTTOM + 40
        self.speedX = 0
        self.speedY = -1
        pygame.time.set_timer(glob.Events.MOVING_END, 1200, 0)
        pygame.time.set_timer(glob.Events.GOD_MODE_END, 2000, 0)
        pygame.time.set_timer(glob.Events.FLASHING, 100)


class _Bomb:
    def __init__(self, speed, angle, radius, relative_x=None, relative_y=None):
        self.speed = speed
        self.angle = angle
        self.radius = radius
        self.relative_x = relative_x
        self.relative_y = relative_y
        self.attack = None

    def set_attack(self, attack):
        self.attack = attack

    def set_coords(self, x, y):
        self.relative_x = x
        self.relative_y = y


def _init_bomb(bomb_type):
    if bomb_type == 0:
        speed = -5
        radius = 170
        bomb = _Bomb(speed, 0, radius)

        def attack(target):
            if target is None: raise Exception("Target not found!")
            bomb.angle = (bomb.angle + 8) % 180
            for i in range(6):
                glob.Groups.player_bullets.add(
                    Bullet("pellet", target.rect.centerx + cos(radians(i * 60 + bomb.angle)) * radius,
                           target.rect.centery + sin(radians(i * 60 + bomb.angle)) * radius,
                           speed * cos(radians(i * 60 + bomb.angle)), speed * sin(radians(i * 60 + bomb.angle))))
            bomb.set_coords(target.rect.centerx, target.rect.centery)
        bomb.set_attack(attack)
        return bomb
