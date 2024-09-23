"""
Tic Tac Toe Test
"""

from tictactoe import *  # import everything from tictactoe.py
import math


def test_player():
    """
    Test the player function.
    """

    # Test case 1: Initial board (X should play first)
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert player(board) == X

    # Test case 2: One move made by X
    board = [[X, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert player(board) == O

    # Test case 3: Two moves made (X and O)
    board = [[X, O, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert player(board) == X

    # Test case 4: X has made more moves than O
    board = [[X, O, X],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert player(board) == O

    print("All tests for player passed!")


def test_actions():
    """
    Test the actions function.
    """

    # Test case 1: Initial board (all spaces are available)
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert actions(board) == {(0, 0), (0, 1), (0, 2),
                              (1, 0), (1, 1), (1, 2),
                              (2, 0), (2, 1), (2, 2)}

    # Test case 2: Some spaces taken
    board = [[X, O, EMPTY],
             [EMPTY, X, O],
             [EMPTY, EMPTY, EMPTY]]
    assert actions(board) == {(0, 2), (1, 0), (2, 0), (2, 1), (2, 2)}

    # Test case 3: All spaces filled (no actions available)
    board = [[X, O, X],
             [O, X, O],
             [O, X, O]]
    assert actions(board) == set()

    print("All tests for actions passed!")

def test_result():
    # Test 1: Player X makes a move in an empty board
    board1 = initial_state()
    action1 = (0, 0)
    expected_board1 = [[X, EMPTY, EMPTY],
                       [EMPTY, EMPTY, EMPTY],
                       [EMPTY, EMPTY, EMPTY]]
    
    assert result(board1, action1) == expected_board1, "Test 1 Failed"
    assert result(board1, action1) != board1, "Test 1 Failed"

    
    # Test 2: Player O makes a move after Player X has played
    board2 = [[X, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY]]
    action2 = (1, 1)
    expected_board2 = [[X, EMPTY, EMPTY],
                       [EMPTY, O, EMPTY],
                       [EMPTY, EMPTY, EMPTY]]
    
    assert result(board2, action2) == expected_board2, "Test 2 Failed"
    assert result(board2, action2) != board2, "Test 2 Failed"


    # Test 3: Invalid move (cell already occupied)
    board3 = [[X, O, EMPTY],
              [EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY]]
    action3 = (0, 0)
    try:
        result(board3, action3)
        assert False, "Test 3 Failed - Exception should have been raised"
    except Exception as e:
        assert str(e) == "There is no valid space to insert in this cell!", "Test 3 Failed"
    
    # Test 4: Player X makes a move on a partially filled board
    board4 = [[X, O, EMPTY],
              [EMPTY, O, EMPTY],
              [EMPTY, EMPTY, X]]
    action4 = (1, 0)
    expected_board4 = [[X, O, EMPTY],
                       [X, O, EMPTY],
                       [EMPTY, EMPTY, X]]
    
    assert result(board4, action4) == expected_board4, "Test 4 Failed"
    assert result(board4, action4) != board4, "Test 4 Failed"
    
    print("All tests passed!")

def test_winner():
    # Test 1: X wins with a horizontal row
    board1 = [[X, X, X],
              [O, EMPTY, O],
              [EMPTY, EMPTY, EMPTY]]
    assert winner(board1) == X, "Test 1 Failed"

    # Test 2: O wins with a vertical column
    board2 = [[X, O, EMPTY],
              [X, O, EMPTY],
              [EMPTY, O, EMPTY]]
    assert winner(board2) == O, "Test 2 Failed"

    # Test 3: X wins with a diagonal (top-left to bottom-right)
    board3 = [[X, O, EMPTY],
              [EMPTY, X, O],
              [EMPTY, EMPTY, X]]
    assert winner(board3) == X, "Test 3 Failed"

    # Test 4: O wins with a diagonal (top-right to bottom-left)
    board4 = [[X, X, O],
              [X, O, EMPTY],
              [O, EMPTY, EMPTY]]
    assert winner(board4) == O, "Test 4 Failed"

    # Test 5: No winner (game not finished)
    board5 = [[X, O, X],
              [X, EMPTY, O],
              [O, X, O]]
    assert winner(board5) is None, "Test 5 Failed"

    # Test 6: No winner (game is a draw)
    board6 = [[X, O, X],
              [X, O, O],
              [O, X, X]]
    assert winner(board6) is None, "Test 6 Failed"

    # Test 7: Pass in an empty board to see if it handled well
    assert winner(initial_state()) is None, "Test 7 Failed"

    print("All tests passed!")

if __name__ == "__main__":
    test_player()
    test_actions()
    test_result()
    test_winner()

