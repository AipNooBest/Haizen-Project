import pygame

from constants.window import *
from objects.Bullet import Bullet
from objects.glob import groups, events


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((23, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = FRAME_LEFT + FRAME_RIGHT / 2
        self.rect.centery = FRAME_BOTTOM - 40
        self.speedX = 0
        self.speedY = 0
        self.reloaded = True
        self.reload_speed = 60

    def update(self) -> None:
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
            pygame.time.set_timer(events["reloaded_event"], self.reload_speed)
            groups["player_bullets"].add(Bullet("pin", self.rect.centerx - 10, self.rect.y - 15, 0, -speed))
            groups["player_bullets"].add(Bullet("pin", self.rect.centerx + 5, self.rect.y - 15, 0, -speed))
