"""
    Obstruction Game:
        human_symbol = X
        computer_symbol = O
"""
from ui import UI
from board import Board
from computer_player import ComputerPlayer
from strategy import Strategy
from tests.test_board import TestBoard
from tests.test_cell import TestCell
from tests.test_computer_player import TestComputerPlayer
import unittest


if __name__ == "__main__":
    board = Board()
    strategy = Strategy()
    game = ComputerPlayer(board, strategy)
    #unittest.main()
    ui = UI(game, 'X', 'O')
    ui.run()
