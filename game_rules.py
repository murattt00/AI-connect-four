import numpy as np

Row_count = 6
Column_count = 7

Player_piece = 1
Ai_piece = -1
Empty = 0

def create_board():
    board = np.zeros((Row_count, Column_count))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece
    return board

def is_valid_location(board, col):
    return board[Row_count-1][col] == 0

def get_next_open_row(board, col):
    for r in range(Row_count):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))
    print("-----------------")
    print(" 0 1 2 3 4 5 6")

def check_win(board, piece):
   
    for c in range(Column_count-3):
        for r in range(Row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    
    for c in range(Column_count):
        for r in range(Row_count-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    for c in range(Column_count-3):
        for r in range(Row_count-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    for c in range(Column_count-3):
        for r in range(3, Row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def get_valid_locations(board):
    valid_locations = []
    for col in range(Column_count):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations

def is_terminal_node(board):
    return check_win(board, Player_piece) or check_win(board, Ai_piece) or len(get_valid_locations(board)) == 0
