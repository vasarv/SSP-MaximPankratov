import pygame as pg

pg.init()

# класс экрана игры
class ScreenGame:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.color = (0, 76, 153)
        self.win = pg.display.set_mode((self.width, self.height))
        self.tick = 60

    def chahge_screen(self, width, height, color = None):
        self.width = width
        self.height = height
        if color:
            self.color = color

# экземпляр класса
sc = ScreenGame()

# класс количества раундов
class NumberRounds:

    def __init__(self):
        self.number_rounds = 0

    def change_rounds(self, rounds):
        self.number_rounds = rounds

    def decrease_rounds(self):
        if self.number_rounds > 0:
            self.number_rounds -= 1
       


nr = NumberRounds()

# класс подсчета очков
class Scores:
    def __init__(self):
        self.pl_score = 0
        self.comp_score = 0

    def change_scores(self, player_score = 0, computer_score = 0):
        self.pl_score += player_score
        self.comp_score += computer_score

scores = Scores()

# флаг выбора пользователя
class UsersChoice:

    def __init__(self):
        self.users_choice = False

    def change_users_choice(self):
        self.users_choice = True if self.users_choice == False else False


uc = UsersChoice()

# шрифты
class Fonts:
    def __init__(self):
        self.roboto = pg.font.SysFont('roboto', 48)
        self.arial = pg.font.SysFont('arial', 36)

ft = Fonts()

# цвета
class Colors:

    def __init__(self):
        self.white = (255, 255, 225)
        self.yellow = (255, 255, 0)


colors = Colors()

# флаг старта раунда
class StartGame:

    def __init__(self):
        self.start_game = False

    def change_start_game(self):
        self.start_game = True if self.start_game == False else False


sg = StartGame()

