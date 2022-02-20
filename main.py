import pygame

import objects.SpellCard
from constants.window import *
from objects.Enemy import Enemy
from objects.Player import Player
from objects.glob import groups, events
import constants.playscreen

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)
pygame.display.set_caption("Haizen Project")
clock = pygame.time.Clock()
constants.playscreen.init()
player = Player()
enemy = Enemy(40)
groups["all_sprites"].add(player)
groups["all_sprites"].add(enemy)
groups["mobs"].add(enemy)


# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            player.reloaded = True
            pygame.time.set_timer(events["reloaded_event"], 0)
        if event.type == pygame.USEREVENT + 1:
            enemy.attack()
        if event.type == pygame.USEREVENT + 2:
            objects.SpellCard.loop()

    groups["all_sprites"].update()

    screen.fill(BLACK)
    groups["all_sprites"].draw(screen)
    pygame.display.flip()

pygame.quit()
