from texttable import Texttable
from collection import Collection
from cell import Cell


class Board:
    def __init__(self, rows: int = 6, columns: int = 6):
        self.__rows = rows
        self.__columns = columns
        self.__data = self.create_board()

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__columns

    def create_board(self):
        """
        Creates the board based on the __rows and __columns
        :return: a board of dimensions __rows x __columns
        """
        return Collection([Collection([Cell() for column in range(self.__columns)]) for row in range(self.__rows)])

    def __getitem__(self, key):
        """
        Returns the list __data[key] representing the number of appearances of key row in the __data matrix
        """
        return self.__data[key]

    def __str__(self):
        """
        The string representation of a board
        """
        representation = Texttable()
        header = [''] + [chr(ord('A') + index) for index in range(self.__columns)]
        representation.header(header)

        for row in range(self.__rows):
            row_data = [str(row + 1)] + [self.__data[row][column] for column in range(self.__columns)]
            representation.add_row(row_data)
        return representation.draw()
