# Battlesnake.py
# represents a battlesnake game
# Properties:
#   1. game_state -> json data with stuff like food position, snake position, height...
#   2. valid_moves -> each move request we find valid moves to choose randomly from (for now)
#   3. prev_head -> used to save the position of my head on the previous move.
#                       Using the current we can get our direction
#   4. me -> list of coordinates that represents my position on the board
#
import random
from coordinates import Coordinate


class Battlesnake:
    # default
    def __init__(self):
        self.__game_state = {}
        self.__valid_moves = []
        self.__prev_head = []  # a point (x,y)
        self.__me = []

    # random move approach to get started
    # pick a random valid move
    def move(self):
        self.set_valid_moves()

        # save current head position
        self.set_prev_head(self.get_noggin())

        return random.choice(self.__valid_moves)

    # find valid moves (don't go into walls or myself for now)
    def set_valid_moves(self):
        # start with all moves being valid and remove invalid as we go
        self.__valid_moves = ["left", "right", "up", "down"]

        # avoid walls / myself
        self.basic_avoidance()

        return random.choice(self.__valid_moves)

    # remove moves that will turn back into myself
    #   and walls
    def basic_avoidance(self):
        # get which way we are facing
        direction = self.get_direction()
        new_head = self.get_noggin()

        # ** these are not one or the other **
        # at right wall (x = length - 1), DONT move RIGHT
        # if direction is left, also DONT move RIGHT
        if (new_head['x'] == self.get_width() - 1 or direction == "left"):
            self.__valid_moves.remove("right")

        # at left wall (x = 0), DONT move LEFT
        # if direction is right, also DONT move LEFT
        if (new_head['x'] == 0 or direction == "right"):
            self.__valid_moves.remove("left")

        # at bottom wall (y = height - 1), DONT move DOWN
        # if direction is up, also DONT move DOWN
        if (new_head['y'] == self.get_height() - 1 or direction == "up"):
            self.__valid_moves.remove("down")

        # top wall (y = 0), DONT move UP
        # if direction is down, also DONT move UP
        if (new_head['y'] == 0 or direction == "down"):
            self.__valid_moves.remove("up")

# region GETTERS and some SETTERS

    # get the direction we're moving in
    # this should only be called after self.__game_state is updated
    # REWORK
    def get_direction(self):
        new_head = self.get_noggin()
        direction = str()
        # naive approach
        # previous x is one to the left of new one -> we're facing right
        if (self.__prev_head['x'] + 1 == new_head['x']):
            direction = "right"

        # previous x is one to the right of new one -> we're facing left
        if (self.__prev_head['x'] - 1 == new_head['x']):
            direction = "left"

        # previous y is one above new one -> facing down
        if (self.__prev_head['y'] + 1 == new_head['y']):
            direction = "down"

        # previous y is below new one -> facing up
        if (self.__prev_head['y'] - 1 == new_head['y']):
            direction = "up"

        # empty string returned on first move
        return direction

    # set previous head (x,y)
    def set_prev_head(self, prev_head):
        self.__prev_head = prev_head

    # set game state
    def set_state(self, game):
        self.__game_state = game

    # get enemies (includes me)
    # REWORK
    # TODO loop through, testing for me -> (head will be at same posiiotn) to remove myself
    def get_enemies(self):
        return self.__game_state['board']['snakes']

    # set me from game state
    def set_me(self):
        self.__me.clear()
        # for each json {'x': <> , 'y': <>} transform into Coordinate
        #   and add to self.__me
        for coord in self.__game_state['you']['body']:
            self.__me.append(Coordinate({'x': coord['x'], 'y': coord['y']}))

    # get me (testing)
    def get_me(self):
        return self.__me

    # get the position of my head
    def get_noggin(self):
        head = self.__me[0]
        return head

    # get the position of my tail
    def get_tail(self):
        tail = self.__me[len(self.__me) - 1]
        return tail

    # get the width of the board
    def get_width(self):
        return self.__game_state['board']['width']

    # get the height of the board
    def get_height(self):
        return self.__game_state['board']['height']

    # get valid moves (for testing)
    def get_valid(self):
        return self.__valid_moves

# endregion
