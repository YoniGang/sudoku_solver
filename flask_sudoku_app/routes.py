# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:19:44 2020

@author: yonig
"""

from flask import request, jsonify, render_template
from flask_sudoku_app import app
import flask_sudoku_app.status_codes as status
from flask_sudoku_app.sudoku_solver import Grid
import json
# import re

@app.route("/", methods=['GET'])
def home():
    reset_grid = [[0]*9]*9
    return render_template("index.html", data=reset_grid), status.OK

@app.route("/get_grid", methods=['GET'])
def get_grid():
    try:
        with open('grid.txt', 'rb') as f:
            grid = json.loads(f.read())
    except Exception as e:
        return jsonify({'Exception': str(e)}), status.BAD_REQUEST
    
    # grid = Grid(list(grid.values()))
    return render_template("index.html", data=list(grid.values())), status.OK
    # return str(grid), status.OK
    # return jsonify({'Success': 'Hopully the board will show here in the future'}), status.OK
    
@app.route("/upload_grid", methods=['POST'])
def upload_grid():
    if not request.is_json:
        return jsonify({'Error': 'Request does not contain a json'}), status.BAD_REQUEST
    
    content = request.get_json()
    with open('grid.txt', 'wb') as f:
        f.write(json.dumps(content))
    
    return jsonify({'Success': 'Grid updated'}), status.OK


@app.route("/solve_grid", methods=['GET'])
def solve_grid():
    try:
        with open('grid.txt', 'rb') as f:
            grid = json.loads(f.read())
    except Exception as e:
        return jsonify({'Exception': str(e)}), status.BAD_REQUEST
    
    grid = Grid(list(grid.values()))
    ans = grid.solve_grid()
    # if ans:
    return render_template("index.html", data=list(grid.list_repr())), status.OK
    # else:
        