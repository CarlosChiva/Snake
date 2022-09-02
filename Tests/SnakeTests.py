import unittest
from SnakeBody import Snake
from Punto import Punto

class MyTestCase(unittest.TestCase):
    punto=Punto(3,5)
    def setUp(self):
        snake=Snake(self.punto)
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
