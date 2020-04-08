# server.py
# implementation of battlesnake (bs) api for maximum destruction of other snakes
# april 2020
from flask import Flask, request, jsonify
import json
from Battlesnake import Battlesnake

# for testing
from coordinates import Coordinate


app = Flask(__name__)

game = Battlesnake()

# some constants
HEIGHT = 0
WIDTH = 1
FOOD = 2
ENEMIES = 3
ME = 4

# snake birth
@app.route('/')
def index():
    return "IM ALIVE MUAHAHAHAA"


# called to see if snake is functional
# only needs ok status response
@app.route('/ping')
def ping():
    return jsonify(success=True), 200


# called when we enter a game
@app.route('/start', methods=['GET', 'POST'])
def start():
    data = request.get_json()
    # set up game
    game.set_state(data)
    game.set_me()
    game.set_prev_head(game.get_noggin())

    return jsonify(color="#E8FF00", headType="tongue",
                   tailType="small-rattle")


# called to get a move response
@app.route('/move', methods=['GET', 'POST'])
def move():
    data = request.get_json()

    game.set_state(data)

    move = game.move()

    return jsonify(move=move)


# snake died or championed
@app.route('/end', methods=['POST'])
def end():
    return jsonify(success=True), 200


if __name__ == '__main__':
    app.run()
