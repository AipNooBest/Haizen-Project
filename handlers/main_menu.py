import sys
import pygame
import handlers.playscreen

from objects import Global
from UI.elements.Text import Text
from constants.game_states import *
from constants.window import *


def handle(event):
    global selected
    if Global.Variables.game_state != GameStates.MAIN_MENU: return
    Global.Variables.screen.fill("black")
    if event.type == pygame.KEYDOWN:
        if state == MenuState.START:
            if event.key == pygame.K_z:
                if selected == 0:
                    _unload()
                    handlers.playscreen.init()
                    Global.game_state = 1
                    return
                elif selected == 1:
                    _unload()
                    _open_settings()
                    selected = 0
                else:
                    sys.exit()

        elif state == MenuState.SETTINGS:
            if event.key == pygame.K_RIGHT or (event.key == pygame.K_z and not selected == len(buttons)-1):
                if selected == 0:
                    Global.lives = (Global.lives + 1) % 5
                    buttons[0].change_text(text="Жизни : %i" % Global.lives)
                elif selected == 1:
                    Global.bombs = (Global.bombs + 1) % 5
                    buttons[1].change_text(text="Бомбы : %i" % Global.bombs)
                elif selected == 2:
                    Global.bomb_type = (Global.bomb_type + 1) % 2
                    buttons[2].change_text(text="Тип бомб : %i" % Global.bomb_type)
                elif selected == 3:
                    Global.difficulty = (Global.difficulty + 1) % 2
                    if Global.difficulty == Global.Difficulty.NORMAL:
                        difficulty = "НОРМАЛЬНАЯ"
                    else:
                        difficulty = "СЛОЖНАЯ"
                    buttons[3].change_text(text="Сложность : %s" % difficulty)
            elif event.key == pygame.K_LEFT:
                if selected == 0:
                    Global.lives = (Global.lives - 1) % 5
                    buttons[0].change_text(text="Жизни : %i" % Global.lives)
                elif selected == 1:
                    Global.bombs = (Global.bombs - 1) % 5
                    buttons[1].change_text(text="Бомбы : %i" % Global.bombs)
                elif selected == 2:
                    Global.bomb_type = (Global.bomb_type - 1) % 2
                    buttons[2].change_text(text="Тип бомб : %i" % Global.bomb_type)
                elif selected == 3:
                    Global.difficulty = (Global.difficulty - 1) % 2
                    if Global.difficulty == Global.Difficulty.NORMAL:
                        difficulty = "НОРМАЛЬНАЯ"
                    else:
                        difficulty = "СЛОЖНАЯ"
                    buttons[3].change_text(text="Сложность : %s" % difficulty)
            elif event.key == pygame.K_z:
                if selected == 4:
                    _unload()
                    init()
            elif event.key == pygame.K_x:
                buttons[selected].rect.x = DEF_BUTTON_X
                buttons[selected].change_text(None, None, None, "grey")
                selected = 4

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
    labels = ["Жизни : %i" % Global.lives, "Бомбы : %i" % Global.bombs,
              "Тип бомб : %i" % Global.bomb_type, "Сложность : %s" % "НОРМАЛЬНАЯ", "Назад"]
    for i in range(len(labels)):
        buttons.append(Text(labels[i], font, 32, "grey", (DEF_BUTTON_X, HEIGHT / 2 + i*40), "right"))
