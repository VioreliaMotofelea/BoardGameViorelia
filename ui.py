from point import Point
from computer_player import CoordinatesError, ComputerPlayerError


class UIError(Exception):
    """
    Custom exception class representing a user input error
    """
    pass


class UI:
    """
    ConsoleUI class implements the console UI. This UI can be chosen from the settings.properties file of the application
    """
    def __init__(self, game, human_symbol, computer_symbol):
        self.__game = game
        self.__human_symbol = human_symbol
        self.__computer_symbol = computer_symbol

    def human_turn(self):
        """
        Perform a human move
        """
        move_completed = False
        while not move_completed:
            try:
                move_completed = True
                print("Human's turn: ")
                coordinates = self.read_human_move()
                game_over = self.__game.human_move(self.__human_symbol, coordinates)
                print('Human move successfully performed.\n')
                return game_over
            except (CoordinatesError, UIError) as inputError:
                print(inputError)
                move_completed = False

    def computer_turn(self):
        """
        Perform a computer move
        """
        print("Computer's turn: ")
        print('Computer move successfully performed.\n')
        return self.__game.computer_move(self.__computer_symbol)

    @staticmethod
    def read_human_move():
        """
        Gets the coordinates of a human move. The human introduce the specific square
        :return: a point having the (x, y) coordinates of a human move
        :raises: UserInputError if the given coordinates are not positive integers
        """

        target = input("Where to place? >>> ")
        if not target[1].isdigit() or not target[0].isalpha():
            raise UIError("Invalid input!\n")
        x_coordinate = int(target[1]) - 1
        y_coordinate = ord(target[0]) - ord('A')

        return Point(int(x_coordinate), int(y_coordinate))

    def draw_board(self):
        """
        Draws the game board
        """
        print(self.__game.board)

    def run(self):
        """
        Runs the UI
        """
        try:
            symbol_turn = {self.__human_symbol: self.human_turn, self.__computer_symbol: self.computer_turn}
            game_over = False

            while not game_over:
                self.draw_board()
                game_over = symbol_turn['X']()
                self.draw_board()
                if game_over:
                    print('YOU W0N! Player X won the game.\n')
                else:
                    game_over = symbol_turn['O']()
                    if game_over:
                        print('YOU LOST! Player O won the game.\n')
            self.draw_board()
        except (UIError, CoordinatesError, ComputerPlayerError) as error:
            print(f"{str(error)}\n")
        except Exception as exception:
            print(f"Unexpected exception occurred: {str(exception)}.\n")
