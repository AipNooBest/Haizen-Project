import sys
import pygame
import constants.playscreen
import objects.glob

from objects.Text import Text
from constants.window import *


selected = 0
buttons = []
DEF_BUTTON_X = WIDTH - 90


def init():
    Text("Haizen Project", "EoSD", 35, "white", (WIDTH / 2, HEIGHT / 4), "center")
    buttons.append(Text("Start", "EoSD", 35, "grey", (DEF_BUTTON_X, HEIGHT / 2), "right"))
    buttons.append(Text("Quit", "EoSD", 35, "grey", (DEF_BUTTON_X, HEIGHT / 2 + 40), "right"))


def handle(event):
    global selected
    if objects.glob.game_state != 0: return
    objects.glob.screen.fill("black")
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            buttons[selected].rect.x = DEF_BUTTON_X
            buttons[selected].change_text(None, None, None, "grey")
            selected += 1
        if event.key == pygame.K_UP:
            buttons[selected].rect.x = DEF_BUTTON_X
            buttons[selected].change_text(None, None, None, "grey")
            selected -= 1
        if event.key == pygame.K_z:
            if selected == 0:
                unload()
                constants.playscreen.init()
                objects.glob.game_state = 1
                return
            else: sys.exit()

    selected %= len(buttons)
    buttons[selected].rect.x = DEF_BUTTON_X - 20
    buttons[selected].change_text(color="white")


def unload():
    objects.glob.groups["all_sprites"].empty()
    buttons.clear()
