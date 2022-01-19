# wsgi.py
# pylint: disable=missing-docstring

<<<<<<< HEAD
=======
import imp
>>>>>>> http-server
from flask import Flask, render_template, request
from game import Game

app = Flask(__name__)

@app.route('/')
def home():
    game = Game()
<<<<<<< HEAD
    return render_template('home.html', grid=game.grid)

@app.route('/check', methods=["POST"])
def check():
    game = Game()
=======
>>>>>>> http-server
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word)