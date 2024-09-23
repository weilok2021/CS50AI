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
    num_X = 0
    num_O = 0
    for row in board:
        for shape in row:
            if shape == X:
                num_X += 1
            if shape == O:
                num_O += 1
    if num_X == num_O:
        return X
    elif num_O < num_X:
        return O
    else:
        return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):  # index i represents numbers of rows
        for j in range(len(board[i])):  # index j represents numbers of columns in each row
            if board[i][j] == EMPTY:
                actions.add((i, j))  # add available space to actions set
    return actions
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    if i >= len(board) or j >= len(board) or i < 0 or j < 0:
        raise Exception("This is not a valid move as index out of bound!")
    # if no empty space in location (i, j), raise exception
    if board[i][j] != EMPTY:
        raise Exception("There is no valid space to insert in this cell!")

    # make a deep copy of the original board (copy the outer and also the inner lists)
    board_copy = copy.deepcopy(board)
    # either turn of player X or player O
    X_or_O = player(board_copy)
    board_copy[i][j] = X_or_O
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # if board[i][j] == board[i][j+1] == board[i][j+2] domain:i = (0,1,2), j = 0
    #    board[i][j] == board[i+1][j] == board[i+2][j] domain: i = 0, j = (0,1,2)
    #    board[i][j] == board[i+1][j+1] == board[i+2][j+2] domain: i = 0, j = 0
    #    board[i][j] == board[i-1][j+1] == board[i-2][j+2] domain: i = 2, j = 0

    # diagonal win conditions
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] is not None:
        return board[2][0]

    for i in range(len(board)):
        # same row win condition
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        # same column win condition
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    # if none of this win conditions has triggered, means the game is still in progress or it's is a tie game
    return None


def has_space(board):
    for i in range(len(board)):  # index i represents numbers of rows
        for j in range(len(board[i])):  # index j represents numbers of columns in each row
            if board[i][j] == EMPTY:
                return True
    return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if winner is out, the game is over
    if winner(board):
        return True
    # otherwise, checks is there empty cells, if yes the game is not over yet.
    else:
        if has_space(board):
            return False
        else:
            return True


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
    If the board is a terminal board, this minimax function should return None.
    """

    def max_value(board):
        if terminal(board):
            return utility(board)
        # a number represents negative infinity in python
        v = -float("inf")
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
            # this is the action that bring greatest value after
            # recursively considering subsequent actions of min player
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        # a number represents infinity in python
        v = float("inf")
        for action in actions(board):
            # this is the action that bring smallest value after
            # recursively considering the subsequent actions of max player
            v = min(v, max_value(result(board, action)))
        return v

    best_action = None

    if terminal(board):
        return None

    curr_player = player(board)

    if curr_player == X:
        best_value = -float("inf")
        for action in actions(board):
            # this line of code logic is X player consider after I make this move which is returned by result(board, action)
            # what will the opponent O player do? They will try to minimize their utility! (Assume the opponent make optimize move)
            # Thus, we find the maximum of these values.
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
    elif curr_player == O:
        best_value = float("inf")
        for action in actions(board):
            # this is the same logic compare as the above Max player
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
    return best_action
