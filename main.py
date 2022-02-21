import pygame
import objects.SpellCard
import constants.playscreen
import constants.startscreen

from constants.window import *
from objects.Enemy import Enemy
from objects.Player import Player
from objects.glob import groups, events, screen

# Инициализация
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Haizen Project")
clock = pygame.time.Clock()
state = 0
constants.startscreen.init()
player = Player()
enemy = Enemy(80)


# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if state == 0:
            constants.startscreen.handle(event)
        elif state == 1:
            constants.playscreen.handle(event)
        if event.type == pygame.USEREVENT:
            player.reloaded = True
            pygame.time.set_timer(events["reloaded_event"], 0)
        if event.type == pygame.USEREVENT + 1:
            enemy.attack()
        if event.type == pygame.USEREVENT + 2:
            objects.SpellCard.loop()

    groups["all_sprites"].update()
    groups["all_sprites"].draw(screen)
    pygame.display.flip()

pygame.quit()
