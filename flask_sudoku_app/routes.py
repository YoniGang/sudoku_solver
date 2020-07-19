# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:19:44 2020

@author: yonig
"""

from flask import request, jsonify
from flask_sudoku_app import app
import flask_sudoku_app.status_codes as status
# import re

@app.route("/", methods=['GET'])
def home():
   return 'Welcome'

@app.route("/get_grid", methods=['GET'])
def get_grid():
    if not request.is_json:
        return jsonify({'Error': 'Request does not contain a json'}), status.BAD_REQUEST
    return jsonify({'Success': 'Hopully the board will show here in the future'}), status.OK
