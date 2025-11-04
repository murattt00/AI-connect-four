import math
import random
from game_rules import *

def evaluate_window(window, piece):
    score = 0
    opp_piece = Player_piece if piece == Ai_piece else Ai_piece

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(Empty) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(Empty) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(Empty) == 1:
        score -= 4

    return score

def score_position(board, piece):
    score = 0

    center_array = [int(i) for i in list(board[:, Column_count // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    for r in range(Row_count):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(Column_count - 3):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

    for c in range(Column_count):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(Row_count - 3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)

    for r in range(Row_count - 3):
        for c in range(Column_count - 3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    for r in range(3, Row_count):
        for c in range(Column_count - 3):
            window = [board[r-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if check_win(board, Ai_piece):
                return (None, 100000000000000)
            elif check_win(board, Player_piece):
                return (None, -10000000000000)
            else: 
                return (None, 0)
        else: 
            return (None, score_position(board, Ai_piece))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, Ai_piece)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, Player_piece)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value