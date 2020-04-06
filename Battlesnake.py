# Battlesnake.py
# a battlesnake game class
#
import random


class Battlesnake:
    # default
    def __init__(self):
        self.__game = {}
        self.__valid_moves = []
        self.__direction = []  # a point (x,y)

    # random move approach to get started
    # pick a random valid move
    def move(self):
        self.set_valid_moves()
        return random.choice(self.__valid_moves)

    # find valid moves (don't go into walls or myself for now)
    def set_valid_moves(self):
        self.__valid_moves.clear()
        head = self.get_noggin()
        x = head[0]
        y = head[1]

        # avoid walls naively?
        # head at bottom wall
        if (y != self.get_height() - 1):
            self.__valid_moves.append("down")
        # head at top wall
        if (y != 0):
            self.__valid_moves.append("up")
        # head at right wall
        if (x != self.get_width() - 1):
            self.__valid_moves.append("right")
        # head at left wall
        if (x != 0):
            self.__valid_moves.append("left")

        self.remove_invalid(self.get_direction())

    # remove the opposite to our direction from valid moves
    def remove_invalid(self, direction):
        if (direction == "left"):
            self.__valid_moves.remove("right")
        elif (direction == "right"):
            self.__valid_moves.remove("left")
        elif (direction == "up"):
            self.__valid_moves.remove("down")
        else:
            self.__valid_moves.remove("up")


# region GETTERS and some SETTERS

    # get the direction we're moving in

    def get_direction(self):
        new_head = self.get_noggin()
        direction = str()
        # naive approach
        # previous x is greater than current x
        if (self.__direction[0] > new_head[0]):  # moving left
            direction = "left"
        # previous x is less than current x
        elif (self.__direction[0] < new_head[0]):  # moving right
            direction = "right"
        # previous y is greater than current y
        elif (self.__direction[1] > new_head[1]):  # moving up
            direction = "up"
        else:  # moving down OR it's first move and we don't have a direction yet
            direction = "down"
        return direction

    # set direction
    def set_direction(self, direction):
        self.__direction = direction

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

    # get the position of my tail
    def get_tail(self):
        body = self.__game['you']['body']
        return body[len(body) - 1]['x'], body[len(body) - 1]['y']

# endregion
