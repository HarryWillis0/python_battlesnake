# server.py
# implementation of battlesnake (bs) api for maximum destruction of other snakes
# april 2020
from flask import Flask, request, jsonify
import json
app = Flask(__name__)

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
    # set up snake
    return jsonify(color="#E8FF00", headType="tongue",
                   tailType="small-rattle")


# called to get a move response
@app.route('/move', methods=['GET', 'POST'])
def move():
    # prosess data
    processed = processState(request.get_json())
    height = processed[HEIGHT]
    width = processed[WIDTH]
    food = processed[FOOD]
    enemies = processed[ENEMIES]
    me = processed[ME]

    # TODO DECIDE HOW TO MOVE

    return jsonify(processed)


# snake died or championed
@app.route('/end', methods=['POST'])
def end():
    return jsonify(success=True), 200


# process board state and extract importatnt values
def processState(data):
    board = data.get('board')
    height = board.get('height')
    width = board.get('width')
    food = board.get('food')
    enemies = board.get('snakes')
    me = data.get('you')

    return height, width, food, enemies, me


if __name__ == '__main__':
    app.run(debug=True)
