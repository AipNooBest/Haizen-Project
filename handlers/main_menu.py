import sys
import pygame
import handlers.playscreen

from objects import glob
from objects.Text import Text
from constants.game_states import *
from constants.window import *
from enum import IntEnum


selected = 0
buttons = []
DEF_BUTTON_X = WIDTH - 90
state: int
font = "Segoe Script"


class MenuState(IntEnum):
    START = 0
    SETTINGS = 1


def init():
    global state
    state = MenuState.START
    Text("Haizen Project", font, 32, "white", (WIDTH / 2, HEIGHT / 4), "center")
    buttons.append(Text("Старт", font, 32, "grey", (DEF_BUTTON_X, HEIGHT / 2), "right"))
    buttons.append(Text("Настройки", font, 32, "grey", (DEF_BUTTON_X, HEIGHT / 2 + 40), "right"))
    buttons.append(Text("Выход", font, 32, "grey", (DEF_BUTTON_X, HEIGHT / 2 + 80), "right"))


def handle(event):
    global selected
    if glob.game_state != GameStates.MAIN_MENU: return
    glob.screen.fill("black")
    if event.type == pygame.KEYDOWN:
        if state == MenuState.START:
            if event.key == pygame.K_z:
                if selected == 0:
                    _unload()
                    handlers.playscreen.init()
                    glob.game_state = 1
                    return
                elif selected == 1:
                    _unload()
                    _open_settings()
                    selected = 0
                else:
                    sys.exit()

        elif state == MenuState.SETTINGS:
            if event.key == pygame.K_z:
                if selected == 0:
                    glob.lives = (glob.lives + 1) % 5
                    buttons[0].change_text(text="Жизни : %i" % glob.lives)
                elif selected == 1:
                    glob.bombs = (glob.bombs + 1) % 5
                    buttons[1].change_text(text="Бомбы : %i" % glob.bombs)
                elif selected == 2:
                    _unload()
                    init()
            elif event.key == pygame.K_x:
                if selected == 0:
                    glob.lives = (glob.lives - 1) % 5
                    buttons[0].change_text(text="Жизни : %i" % glob.lives)
                elif selected == 1:
                    glob.bombs = (glob.bombs - 1) % 5
                    buttons[1].change_text(text="Бомбы : %i" % glob.bombs)

        if event.key == pygame.K_DOWN:
            buttons[selected].rect.x = DEF_BUTTON_X
            buttons[selected].change_text(None, None, None, "grey")
            selected += 1
        if event.key == pygame.K_UP:
            buttons[selected].rect.x = DEF_BUTTON_X
            buttons[selected].change_text(None, None, None, "grey")
            selected -= 1
    selected %= len(buttons)
    buttons[selected].rect.x = DEF_BUTTON_X - 20
    buttons[selected].change_text(color="white")


def _open_settings():
    global state
    state = MenuState.SETTINGS
    Text("Haizen Project", font, 32, "white", (WIDTH / 2, HEIGHT / 4), "center")
    buttons.append(Text("Жизни : %i" % glob.lives, font, 32, "grey", (DEF_BUTTON_X, HEIGHT / 2), "right"))
    buttons.append(Text("Бомбы : %i" % glob.bombs, font, 32, "grey", (DEF_BUTTON_X, HEIGHT / 2 + 40), "right"))
    buttons.append(Text("Назад", font, 32, "grey", (DEF_BUTTON_X, HEIGHT / 2 + 80), "right"))


def _unload():
    glob.Groups.all_sprites.empty()
    buttons.clear()
