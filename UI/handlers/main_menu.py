import pygame

from constants.window import *
from UI.elements.Text import Text
from UI.elements.Button import Button
from UI.handlers.play_screen import PlayScreen
from objects import Global

default_x = WIDTH - 90


def change_page(func):
    def wrapper(self: MainMenu):
        Global.Groups.all_sprites.empty()
        self.selected = 0
        self.buttons.clear()
        func(self)
        self.buttons[self.selected].select() if len(self.buttons) != 0 else None
    return wrapper


class MainMenu:
    def __init__(self):
        self.buttons = []
        self.selected = 0
        self._open_main_menu(self)

    def handle(self, event):
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_UP):
            self.buttons[self.selected].deselect()
            self.selected += 1 if event.key == pygame.K_DOWN else -1
            self.selected %= len(self.buttons)
            self.buttons[self.selected].select()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                self.buttons[self.selected].callback()
            elif event.key == pygame.K_x:
                self.buttons[self.selected].deselect()
                self.selected = len(self.buttons) - 1
                self.buttons[self.selected].select()

    @change_page
    def _open_main_menu(self):
        Text("Haizen Project", pygame.font.SysFont("Segoe Script", 40), "white", (WIDTH / 2, HEIGHT / 4), "center")
        self.buttons = [
            Button("Начать", default_x, HEIGHT / 2, self._start_game, alignment="right"),
            Button("Настройки", default_x, HEIGHT / 2, self._open_settings, alignment="right"),
            Button("Выход", default_x, HEIGHT / 2, self._exit_game, alignment="right")
        ]

    @change_page
    def _open_settings(self):
        Text("Настройки", pygame.font.SysFont("Segoe Script", 40), "white", (WIDTH / 2, HEIGHT / 4), "center")
        self.buttons = [
            Button("Жизни", default_x, HEIGHT / 2, self._change_lives, alignment="right"),
            Button("Бомбы", default_x, HEIGHT / 2, self._change_bombs, alignment="right"),
            Button("Тип бомб", default_x, HEIGHT / 2, self._change_bomb_type, alignment="right"),
            Button("Сложность", default_x, HEIGHT / 2, self._change_difficulty, alignment="right"),
            Button("Назад", default_x, HEIGHT / 2, self._open_main_menu, alignment="right")
        ]

    @change_page
    def _start_game(self):
        Global.Variables.game_state = Global.GameStates.PLAYING
        Global.Variables.current_screen = UI.handlers.play_screen.PlayScreen()
        del self

    def _exit_game(self):
        Global.Variables.game_state = Global.GameStates.EXIT

    def _change_lives(self):
        Global.Settings.lives = (Global.Settings.lives + 1) % 5
        self.buttons[self.selected].text_object.change_text(text=f"Жизни : {Global.Settings.lives}")

    def _change_bombs(self):
        Global.Settings.bombs = (Global.Settings.bombs + 1) % 5
        self.buttons[self.selected].text_object.change_text(text=f"Бомбы : {Global.Settings.bombs}")

    def _change_bomb_type(self):
        Global.Settings.bomb_type = (Global.Settings.bomb_type + 1) % 2
        self.buttons[self.selected].text_object.change_text(text=f"Тип бомбы : {Global.Settings.bomb_type}")

    def _change_difficulty(self):
        Global.Settings.difficulty = (Global.Settings.difficulty + 1) % 2
        self.buttons[self.selected].text_object.change_text(text=f"Сложность : {'НОРМАЛЬНАЯ' if Global.Settings.difficulty == 0 else 'СЛОЖНАЯ'}")
