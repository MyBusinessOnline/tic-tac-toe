# api/app.py

from flask import Flask, request, jsonify
from src import game  # you'll use this later

app = Flask(__name__)

@app.route('/')
def home():
    return "Tic-Tac-Toe API is running"

if __name__ == '__main__':
    app.run(debug=True)
