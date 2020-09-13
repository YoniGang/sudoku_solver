from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__) 
    CORS(app)
    with app.app_context():
        from flask_sudoku_app import routes
        return app