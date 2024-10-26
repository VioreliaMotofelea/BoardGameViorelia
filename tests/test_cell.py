import unittest
from cell import Cell

FREE_CELL = 0
BLOCKED_CELL = 1
X_OCCUPIED_CELL = 2
O_OCCUPIED_CELL = 3
TEMPORARILY_OCCUPIED_CELL = 4


class TestCell(unittest.TestCase):
    def setUp(self):
        self.__cell = Cell()

    def test_putX(self):
        self.__cell.move_X()
        self.assertEqual(self.__cell.state, 2)

    def test_putO(self):
        self.__cell.move_O()
        self.assertEqual(self.__cell.state, 3)

    def test_free(self):
        self.__cell.free()
        self.assertEqual(self.__cell.state, 0)

    def test_block(self):
        self.__cell.block()
        self.assertEqual(self.__cell.state, 1)

    def test_str(self):
        self.__cell.move_X()
        self.assertEqual(str(self.__cell), 'X')
