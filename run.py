# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:16:57 2020

@author: yonig
"""


from flask_sudoku_app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)