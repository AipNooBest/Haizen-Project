import pygame

groups = {
    "all_sprites": pygame.sprite.Group(),
    "mobs": pygame.sprite.Group(),
    "bullets": pygame.sprite.Group(),
    "border": pygame.sprite.Group(),
}

events = {
    "reloaded_event": pygame.USEREVENT
}
