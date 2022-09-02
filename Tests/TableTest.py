import unittest
from Table import Table
from SnakeBody import Snake

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.table = Table()

    def test_len_X(self):
        self.assertEqual(15, self.table.XLEN)  # add assertion here

    def test_len_Y(self):
        self.assertEqual(10, self.table.YLEN)  # add assertion here

    def test_isThereSnake(self):
        self.assertIn(self.table.SNAKE,self.table.table)


if __name__ == '__main__':
    unittest.main()
