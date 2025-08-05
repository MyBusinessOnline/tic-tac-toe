# cli/main.py
from src import game

def run_game():
    board = game.create_board()
    game.print_board(board)
    # Add your CLI game loop here

if __name__ == '__main__':
    run_game()
