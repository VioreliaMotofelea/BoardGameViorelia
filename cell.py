from dataclasses import dataclass

FREE_CELL = 0
BLOCKED_CELL = 1
X_OCCUPIED_CELL = 2
O_OCCUPIED_CELL = 3
TEMPORARILY_OCCUPIED_CELL = 4


@dataclass
class Cell:
    state: int = 0

    def move_X(self):
        """
        Change the state of the cell - put X in the cell == 2
        """
        self.state = 2

    def move_O(self):
        """
        Change the state of the cell - put O in the cell == 3
        """
        self.state = 3

    def free(self):
        """
        Change the state of the cell - free the cell == 0
        """
        self.state = 0

    def block(self):
        """
        Change the state of the cell - block the cell == 1
        """
        self.state = 1

    def __str__(self):
        """
        Gets the string representation of a cell object - its value
        :return: string - the representation of a cell object
        """
        state_representation = {0: '', 1: '#', 2: 'X', 3: 'O', 4: 'err'}
        return state_representation[self.state]
