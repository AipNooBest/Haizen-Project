import pygame
import constants.playscreen
import objects.glob

from constants.window import *
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
        self.invincible = False
        self.visible = True
        self.HP = 3
        self.speedX = 0
        self.speedY = 0
        self.reloaded = False
        self.reload_speed = 60
        self.add(objects.glob.groups["all_sprites"])

    def update(self) -> None:
        if pygame.sprite.spritecollide(self, objects.glob.groups["enemy_bullets"], True) and not self.invincible:
            constants.playscreen.update_sprites("PLAYER_HP", "reduce")
            self.HP -= 1
            self.respawn()
            pygame.time.set_timer(objects.glob.events["flashing"], 100)
        if self.HP <= 0:
            self.kill()
        if not self.movable:
            self.rect.x += self.speedX
            self.rect.y += self.speedY
            return
        if not self.visible and not self.invincible:
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
            pygame.time.set_timer(objects.glob.events["reloaded_event"], self.reload_speed)
            objects.glob.groups["player_bullets"].add(Bullet("pin", self.rect.centerx - 10, self.rect.y - 15, 0, -speed))
            objects.glob.groups["player_bullets"].add(Bullet("pin", self.rect.centerx + 5, self.rect.y - 15, 0, -speed))

    def respawn(self):
        self.invincible = True
        self.movable = False
        self.rect.centerx = (FRAME_LEFT + FRAME_RIGHT) / 2
        self.rect.centery = FRAME_BOTTOM + 40
        self.speedX = 0
        self.speedY = -1
        pygame.time.set_timer(objects.glob.events["moving_end"], 1200, 0)
        pygame.time.set_timer(objects.glob.events["invincibility_end"], 2000, 0)
