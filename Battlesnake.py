# Battlesnake.py
# represents a battlesnake game
# Properties:
#   1. game_state -> json data with stuff like food position, snake position, height...
#
# TODO implement finding food strategy

import random
from coordinates import Coordinate


class Battlesnake:
    # default
    def __init__(self, data):
        self.__game_state = data

    # pick a random valid move
    def move(self):
        valid_moves = self.get_valid_moves()
        print(valid_moves)
        return random.choice(valid_moves)

    # find valid moves (don't go into walls or snakes for now)
    def get_valid_moves(self):
        # start with all moves being valid and remove invalid as we go
        valid_moves = ["left", "right", "up", "down"]

        # go remove invalid moves
        self.avoid_walls_and_others(valid_moves)

        return valid_moves

    # removes moves that will turn into walls or other snakes
    def avoid_walls_and_others(self, valid_moves):
        snake = {}
        body = {}
        me = self.__game_state['you']['body']  # list of {'x', 'y'}

        # check walls
        self.check_wall_left(me, valid_moves)
        self.check_wall_right(me, valid_moves)
        self.check_wall_bottom(me, valid_moves)
        self.check_wall_top(me, valid_moves)
        print("VALID MOVES AFTER CHECKING WALLS: ", valid_moves)
        # loop through 'snakes' seeing if a move is invalid
        for snake in self.__game_state['board']['snakes']:  # for each snake
            for body in snake['body']:
                coordinate = Coordinate({'x': body['x'], 'y': body['y']})
                # test to see if each move in valid_moves will turn into an occupide coordinate
                if (valid_moves.count("left") > 0):
                    self.check_left(valid_moves, me, coordinate)
                if (valid_moves.count("right") > 0):
                    self.check_right(valid_moves, me, coordinate)
                if (valid_moves.count("up") > 0):
                    print(
                        f"checking up with ME: {me[0]['x']} and other as {coordinate}")
                    self.check_up(valid_moves, me, coordinate)
                if (valid_moves.count("down") > 0):
                    self.check_down(valid_moves, me, coordinate)

# helpers
    # check_wall_*
    # these check to see if a move would take us out of bounds
    def check_wall_left(self, me, valid_moves):
        if (me[0]['x'] == 0):  # dont move left
            valid_moves.remove("left")

    def check_wall_right(self, me, valid_moves):
        if (me[0]['x'] == self.__game_state['board']['width'] - 1):  # don't move right
            valid_moves.remove("right")

    def check_wall_bottom(self, me, valid_moves):
        if (me[0]['y'] == self.__game_state['board']['height'] - 1):  # don't move down
            valid_moves.remove("down")

    def check_wall_top(self, me, valid_moves):
        if (me[0]['y'] == 0):  # don't move up
            valid_moves.remove("up")

    # check_*
    # these check if moving in a direction will run into an occupied coordinate
    # if the move does, it's removed from the valid_moves list
    # these should only be called on moves that are in valid_moves
    def check_left(self, valid_moves, me, coord):
        # moving head to the left runs into coord
        if (me[0]['x'] - 1 == coord['x'] and me[0]['y'] == coord['y']):
            valid_moves.remove("left")

    def check_right(self, valid_moves, me, coord):
        # moving head to the right runs into coord
        if (me[0]['x'] + 1 == coord['x'] and me[0]['y'] == coord['y']):
            valid_moves.remove("right")

    def check_down(self, valid_moves, me, coord):
        # moving head down runs into coord
        if (me[0]['y'] + 1 == coord['y'] and me[0]['x'] == coord['x']):
            valid_moves.remove("down")

    def check_up(self, valid_moves, me, coord):
        # moving head up runs into coord
        if (me[0]['y'] - 1 == coord['y'] and me[0]['x'] == coord['x']):
            valid_moves.remove("up")
