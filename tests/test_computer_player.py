import unittest
from board import Board
from point import Point
from computer_player import ComputerPlayer, CoordinatesError
from strategy import Strategy

FREE_CELL = 0
BLOCKED_CELL = 1
X_OCCUPIED_CELL = 2
O_OCCUPIED_CELL = 3
TEMPORARILY_OCCUPIED_CELL = 4


class TestComputerPlayer(unittest.TestCase):
    def setUp(self):
        self.__game = ComputerPlayer(Board(), Strategy())

    def test_move(self):
        point = Point(0, 0)
        human_symbol = 'X'
        computer_symbol = 'O'
        board = self.__game.board
        self.__game.human_move(human_symbol, point)

        blockades = [(0, 1), (1, 1), (1, 0)]
        for row in range(board.rows):
            for column in range(board.columns):
                if not row and not column:
                    self.assertEqual(board[row][column].state, 2)
                elif (row, column) in blockades:
                    self.assertEqual(board[row][column].state, 1)
                else:
                    self.assertEqual(board[row][column].state, 0)

        # Checking for an invalid point - we should get an error message
        point = Point(-1, 0)
        self.assertRaises(CoordinatesError, self.__game.human_move, human_symbol, point)
        try:
            self.__game.human_move(human_symbol, point)
        except CoordinatesError as ce:
            self.assertEqual('CoordinatesError: Invalid coordinates.\n', str(ce))

        # Checking for a blocked point - we should get an error message
        point = Point(1, 1)
        self.assertRaises(CoordinatesError, self.__game.human_move, human_symbol, point)
        self.__game.computer_move(computer_symbol)
        counter = 0
        for row in range(board.rows):
            for column in range(board.columns):
                if board[row][column].state == 3:
                    counter += 1
        self.assertEqual(counter, 1)
