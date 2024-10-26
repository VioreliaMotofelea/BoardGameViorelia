from point import Point
from random import randint

FREE_CELL = 0
BLOCKED_CELL = 1
X_OCCUPIED_CELL = 2
O_OCCUPIED_CELL = 3
TEMPORARILY_OCCUPIED_CELL = 4


class Strategy:
    """
    The computer player should move to win the game whenever possible and should block the human player’s
    attempts at 1-move victory, whenever possible. If none of the above cases is present, then the computer
    player takes a valid random move
    """
    def move(self, board):
        """
        Return a cell for a game move, using the game strategy described above
        :param board: the game board
        :return: a random cell for a game move
        """
        winning_move = self.attempt_winning_move(board)
        if winning_move:
            return winning_move

        possible_moves = self.attempt_defensive_move(board)
        if possible_moves:
            return self.make_random_move(possible_moves)

        return self.make_random_move(self.get_free_points(board))

    @staticmethod
    def make_random_move(possible_moves):
        """
        Makes a random move, selecting it from a list of given possible moves
        :param possible_moves: a list of possible moves
        :return: the random move
        """
        return possible_moves[randint(0, len(possible_moves) - 1)]

    def attempt_winning_move(self, board, default_temp_moves=None):
        """
        Attempts to make a winning move, if possible. Temporarily occupies certain cells and check
        if the computer player wins by doing such a move
        :param board: the game board
        :param default_temp_moves: already made temporarily moves, which should not be eliminated during
        this function's execution
        :return: a point, if a winning move exits, None else
        """
        if default_temp_moves is None:
            default_temp_moves = []

        for point in self.get_free_points(board):
            if board[point.x][point.y].state == 0:
                self.temporarily_moves(board, [point] + default_temp_moves)
                if not len(self.get_free_points(board)):
                    self.free_temporary_occupations(board)
                    return point

                self.free_temporary_occupations(board)
        return None

    def attempt_defensive_move(self, board):
        """
        Attempts to make a defensive move or block the human player’s attempts at 1-move victory, if possible
        :param board: the game board
        :return: the list of possible moves that do not let the other player win next round or None if such moves do
        not exist
        """
        possible_moves = []
        for point in self.get_free_points(board):
            if not self.attempt_winning_move(board, [point]):
                possible_moves.append(point)
            self.free_temporary_occupations(board)
        return None if possible_moves == [] else possible_moves

    @staticmethod
    def temporarily_moves(board, points):
        """
        Makes temporarily moves which will be deleted at a certain moment in the future,
        before displaying them to the user
        :param board: the game board
        :param points: the points where the move will be made
        """
        directions = [-1, 0, 1]
        for point in points:
            for row_dir in directions:
                for column_dir in directions:
                    if (point.x + row_dir in range(board.rows) and
                            point.y + column_dir in range(board.columns) and
                            board[point.x + row_dir][point.y + column_dir].state == 0):
                        board[point.x + row_dir][point.y + column_dir].state = 4

    @staticmethod
    def free_temporary_occupations(board):
        """
        Deletes the temporarily moves (i.e., changes the state of the TEMPORARILY_OCCUPIED cells into FREE state)
        :param board: the game board
        """
        for row in range(board.rows):
            for column in range(board.columns):
                if board[row][column].state == 4:
                    board[row][column].state = 0

    @staticmethod
    def get_free_points(board):
        """
        Gets all the free points/cells in the board (i.e., the cell is in FREE state)
        :param board: the game board
        :return: all free points/cells in the board
        """
        return [Point(x, y) for x in range(board.rows) for y in range(board.columns) if board[x][y].state == 0]
