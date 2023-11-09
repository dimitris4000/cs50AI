"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
minmax_memoize = dict()


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
    count_x = 0
    count_o = 0
    for row in board:
        for cell in row:
            if cell == X:
                count_x += 1
            elif cell == O:
                count_o += 1

    return X if count_x == count_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            if cell is EMPTY: actions.append((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]

    for i,row in enumerate(new_board):
        for j,cell in enumerate(row):
            if (i,j) == action:
                if board[i][j] is EMPTY:
                    new_board[i][j] = player(board)
                else:
                    raise Exception("Invalid board action")
            else:
                new_board[i][j] = board[i][j]

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontal
    for i in range(3):
        if board[i][0] is not EMPTY and \
            board[i][0] == board[i][1] and \
            board[i][0] == board[i][2]:
            return board[i][0]

    # Check vertical
    for i in range(3):
        if board[0][i] is not EMPTY and \
            board[0][i] == board[1][i] and \
            board[0][i] == board[2][i]:
            return board[0][i]

    # Check diagonal
    for i in [0,2]:
        if board[1][1] is not EMPTY and \
            board[1][1] == board[0][i] and \
            board[1][1] == board[2][2-i]:
            return board[1][1]

    return None # No winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check for winner
    win = winner(board)
    if win is not None: return True

    # Check for empty cells
    for row in board:
        if any([cell is EMPTY for cell in row]): return False

    return True # No empty cells, No winners


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win is not None:
        return 1 if win == X else -1

    return 0 # No winners


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None

    # possible_actions = actions(board)
    # if player(board) == X:
    #     optimum_action = [-2, None]
    #     for action in possible_actions:

    # else:
    #     optimum_action = [2, None]
    #     for action in possible_actions:
    #         pass

    return actions(board)[0] # REMOVE/EDIT ME! Dummy code.
