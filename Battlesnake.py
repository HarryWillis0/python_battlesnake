# Battlesnake.py
# a battlesnake game class
#
import random


class Battlesnake:
    # default
    def __init__(self):
        self.__game = {}
        self.__valid_moves = []

    # random move approach to get started
    # pick a random valid move
    def move(self):
        self.set_valid_moves()
        return random.choice(self.__valid_moves)

    # find valid moves (don't go into walls for now)
    def set_valid_moves(self):
        self.__valid_moves.clear()
        head = self.get_noggin()
        x = head[0]
        y = head[1]

        # avoid walls naively?
        if (y != self.get_height() - 1):
            self.__valid_moves.append("down")
        if (y != 0):
            self.__valid_moves.append("up")
        if (x != self.get_width() - 1):
            self.__valid_moves.append("right")
        if (x != 0):
            self.__valid_moves.append("left")

# region GETTERS and some SETTERS

    # set game
    def set_game(self, game):
        self.__game = game

    # get height of board
    def get_height(self):
        return self.__game['board']['height']

    # get width of board
    def get_width(self):
        return self.__game['board']['width']

    # get enemies (includes me)
    def get_enemies(self):
        return self.__game['board']['snakes']

    # get me
    def get_me(self):
        return self.__game['you']

    # get the position of my head
    def get_noggin(self):
        return self.__game['you']['body'][0]['x'], self.__game['you']['body'][0]['y']

# endregion
