from point import Point

FREE_CELL = 0
BLOCKED_CELL = 1
X_OCCUPIED_CELL = 2
O_OCCUPIED_CELL = 3
TEMPORARILY_OCCUPIED_CELL = 4


class ComputerPlayerError(Exception):
    pass


class CoordinatesError(ComputerPlayerError):
    pass


class ComputerPlayer:
    def __init__(self, board, strategy):
        self.__board = board
        self.__strategy = strategy

    @property
    def board(self):
        return self.__board

    def game_over(self):
        """
        Checks whether the game is over or not
        :return: true if the game is over, false else
        """
        for row in range(self.__board.rows):
            for column in range(self.__board.columns):
                if self.__board[row][column].state == 0:
                    return False
        return True

    def get_cell_state(self, point):
        """
        Gets the state of the cell having the given coordinates
        :param point: the coordinates of the cell
        :return: the state of the cell having the given coordinates
        """
        return self.__board[point.x][point.y].state

    def validate_move(self, point):
        """
        Validates a move
        :param point: the coordinates of the move
        :raises: CoordinatesError if the move is invalid
        """
        if point.x not in range(self.__board.rows) or point.y not in range(self.__board.columns):
            raise CoordinatesError('CoordinatesError: Invalid coordinates.\n')
        if not self.get_cell_state(point) == 0:
            raise CoordinatesError('CoordinatesError: Cell already occupied.\n')

    def populate_blockades(self, point):
        """
        Blocks the cell around a given point and returns the number of blocked cells
        :param point: the given point
        :return: the number of blocked cells
        """
        blocked_cells = 0
        directions = [-1, 0, 1]
        for row_dir in directions:
            for column_dir in directions:
                if (point.x + row_dir in range(self.__board.rows) and
                        point.y + column_dir in range(self.__board.columns) and Point(0, 0) != Point(row_dir, column_dir)):
                    self.__board[point.x + row_dir][point.y + column_dir].state = 1
                    blocked_cells += 1
        return blocked_cells

    def human_move(self, value, point):
        """
        Attempts to make a human move
        :param value: the player string symbol (can be 'X' or 'O')
        :param point: the coordinates of the attempted move
        :return: true if the game is over after the move, false else
        """
        state_dict = {'X': 2, 'O': 3}
        self.validate_move(point)
        self.__board[point.x][point.y].state = state_dict[value]
        self.populate_blockades(point)
        return self.game_over()

    def computer_move(self, value):
        """
        Attempts to make a computer move
        :param value: the computer string symbol (can be 'X' or 'O')
        :return: true if the game is over after the move, false else
        """
        state_dict = {'X': 2, 'O': 3}
        point = self.__strategy.move(self.__board)
        x = point.x
        y = point.y
        self.__board[x][y].state = state_dict[value]
        self.populate_blockades(Point(x, y))
        return self.game_over()
