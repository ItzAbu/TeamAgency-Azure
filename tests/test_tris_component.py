import pytest
from typing import List, Optional, Union
from frontend.src.components.tris.Tris import (
    WINNING_LINES,
    checkWinner,
)

Player = Union["X", "O"]
Cell = Optional[Player]

@pytest.mark.parametrize("board, expected_winner", [
    (["X", "X", "X", None, None, None, None, None, None], "X"),
    ([None, None, None, "O", "O", "O", None, None, None], "O"),
    ([None, None, None, None, None, None, "X", "X", "X"], "X"),
    (["O", None, None, "O", None, None, "O", None, None], "O"),  # Col 0
    ([None, "X", None, None, "X", None, None, "X", None], "X"),  # Col 1
    ([None, None, "O", None, None, "O", None, None, "O"], "O"),  # Col 2
    (["X", None, None, None, "X", None, None, None, "X"], "X"),  # Diag
    ([None, None, "O", None, "O", None, "O", None, None], "O"),  # Anti diag
])
def test_check_winner(board: List[Cell], expected_winner: Player):
    assert checkWinner(board) == expected_winner

def test_check_winner_tie():
    tie_board = ["X", "O", "X",
                 "X", "O", "O",
                 "O", "X", "X"]
    assert checkWinner(tie_board) == "Tie"

def test_check_winner_none():
    partial_board = ["X", None, "O",
                     None, "X", None,
                     None, None, None]
    assert checkWinner(partial_board) is None