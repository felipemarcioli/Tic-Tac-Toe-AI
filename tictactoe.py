"""
Tic Tac Toe Player
"""

import math
import copy

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

    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid move")

    new_board = copy.deepcopy(board)
    i,j = action
    new_board[i][j] = player(board)
    return new_board

    
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #verificação de winner na horizontal
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    #verficação de winner na vertical
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]

    #verificação de winner na diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    elif board[0][2] == board [1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board [0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return True if winner(board) != None or len(actions(board)) == 0 else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    valor = -math.inf
    for action in actions(board):
        valor = max(valor, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, valor)
        if alpha >= beta:
            break
    return valor

def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    valor = math.inf
    for action in actions(board):
        valor = min(valor, max_value(result(board, action), alpha, beta))
        beta = min(beta, valor)
        if alpha >= beta:
            break
    return valor


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        best_move = None
        best_value = -math.inf
        for action in actions(board):
            valor = min_value(result(board, action), -math.inf, math.inf)
            if valor > best_value:
                best_value = valor
                best_move = action
        return best_move

    else:
        best_move = None
        best_value = math.inf
        for action in actions(board):
            valor = max_value(result(board, action), -math.inf, math.inf)
            if valor < best_value:
                best_value = valor
                best_move = action
        return best_move
