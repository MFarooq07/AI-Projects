"""
Tic Tac Toe Player
"""

import math
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    empty_count = sum(row.count(EMPTY) for row in board)
    if empty_count % 2 == 0 and empty_count != 9:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    pos_act = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                pos_act.add((i, j))
    return pos_act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    p1 = player(board)
    board[action[0]][action[1]] = p1
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if row_win(board) != None:
        return row_win(board)
    elif col_win(board) != None:
        return col_win(board)
    elif diag_win(board) != None:
        return diag_win(board)
    else:
        return None

def row_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
    return None

def col_win(board):
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]
    return None

def diag_win(board):
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    elif EMPTY not in [cell for row in board for cell in row]:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if the game has ended return none
    if terminal(board):
        return None
    pos_act = actions(board)
    # if only one action is possible, return that action
    if len(pos_act) == 1:
        return pos_act.pop()
    # stop other player from winning 
    board_copy = board.copy()
    ai = player(board)
    
    if ai == X:
        best_score = -math.inf  
        for action in pos_act:
            board_copy[action[0]][action[1]] = ai   
            score = minimax_score(board_copy, False)
            if score > best_score:
                best_score = score
                opt_act = action
            board_copy[action[0]][action[1]] = EMPTY
    else:
        best_score = math.inf
        for action in pos_act:
            board_copy[action[0]][action[1]] = ai   
            score = minimax_score(board_copy, True)
            if score < best_score:
                best_score = score
                opt_act = action
            board_copy[action[0]][action[1]] = EMPTY
    return opt_act
            
            
            
    
def minimax_score(board, is_maximizing):
    if terminal(board):
        return utility(board)
    pos_act = actions(board)
    board_copy = board.copy()
    ai = player(board)
    # playing for X
    if is_maximizing:
        best_score = -math.inf
        for action in pos_act:
            board_copy[action[0]][action[1]] = ai
            score = minimax_score(board_copy, False)
            board_copy[action[0]][action[1]] = EMPTY
            best_score = max(score, best_score)
        return best_score
    # playing for O 
    else:
        best_score = math.inf
        for action in pos_act:
            board_copy[action[0]][action[1]] = ai
            score = minimax_score(board_copy, True)
            board_copy[action[0]][action[1]] = EMPTY
            best_score = min(score, best_score)
        return best_score



#
#
#
#
#
#
# #
#         best_score = -math.inf
#         for action in pos_act:
#             board_copy[action[0]][action[1]] = ai
#             score = minimax_score(board_copy, False)
#             board_copy[action[0]][action[1]] = EMPTY
#             if score > best_score:
#                 best_score = score
#                 opt_act = action
#     else:
#         best_score = math.inf
#         for action in pos_act:
#             board_copy[action[0]][action[1]] = ai
#             score = minimax_score(board_copy, True)
#             board_copy[action[0]][action[1]] = EMPTY
#             if score < best_score:
#                 best_score = score
#                 opt_act = action

#     return opt_act


# def minimax_score(board, is_maximizing):
#     if terminal(board):
#         return utility(board)
#     pos_act = actions(board)
#     board_copy = board.copy()
#     if is_maximizing:
#         best_score = -math.inf
#         for action in pos_act:
#             board_copy[action[0]][action[1]] = X
#             score = minimax_score(board_copy, False)
#             board_copy[action[0]][action[1]] = EMPTY
#             best_score = max(score, best_score)
#         return best_score
#     else:
#         best_score = math.inf
#         for action in pos_act:
#             board_copy[action[0]][action[1]] = O
#             score = minimax_score(board_copy, True)
#             board_copy[action[0]][action[1]] = EMPTY
#             best_score = min(score, best_score)
#         return best_score