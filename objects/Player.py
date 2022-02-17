import pygame

from constants.window import *
from objects.Bullet import Bullet
from objects.glob import groups, events


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT - 60
        self.speedX = 0
        self.speedY = 0
        self.reloaded = True
        self.reload_speed = 60

    def update(self) -> None:
        self.speedX = 0
        self.speedY = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedX = -5
        if keystate[pygame.K_RIGHT]:
            self.speedX = 5
        if keystate[pygame.K_UP]:
            self.speedY = -5
        if keystate[pygame.K_DOWN]:
            self.speedY = 5

        if keystate[pygame.K_z]:
            self.shoot()
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        if self.reloaded:
            self.reloaded = False
            pygame.time.set_timer(events["reloaded_event"], self.reload_speed)
            bullet = Bullet(self.rect.centerx, self.rect.y - 15, 0, -20)
            groups["bullets"].add(bullet)
            groups["all_sprites"].add(bullet)
