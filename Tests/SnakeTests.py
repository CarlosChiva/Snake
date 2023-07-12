import unittest
from SnakeBody import Snake
from Punto import Punto


class MyTestCase(unittest.TestCase):
    xValue = 3
    yValue = 5
    punto = Punto(xValue, yValue)

    def setUp(self):
        self.snake = Snake(self.punto)

    def tearDown(self):
        self.snake.body.clear()
        self.punto = Punto(self.xValue, self.yValue)
        print("----------------Siguiente prueba---------------")

    def test_getXpoint_onePoint(self):
        self.assertEqual(self.snake.getXPoint(0),self.xValue)

    def test_getXpoint_moreThanOnePoint(self):
        punto = Punto(self.xValue + 1, self.yValue)
        self.snake.pickingUp(punto)
        self.assertEqual(punto.getXCoordenade(), self.snake.getXPoint(0))

    def test_getYpoint_onePoint(self):
        self.assertEqual(self.yValue, self.snake.getYPoint(0))

    def test_getYpoint_moreThanOnePoint(self):
        punto = Punto(self.xValue, self.yValue + 1)
        self.snake.pickingUp(punto)
        self.assertEqual(punto.getYCoordenade(), self.snake.body[0].getYCoordenade())

    def test_pickingUp_XCoordenade(self):
        punto = Punto(self.xValue + 1, self.yValue)
        self.snake.pickingUp(punto)
        self.assertEqual(punto.getXCoordenade(), self.snake.getXPoint(0))

    def test_pickingUp_YCoordenade(self):
        punto = Punto(self.xValue, self.yValue + 1)
        self.snake.pickingUp(punto)
        self.assertEqual(punto.getYCoordenade(), self.snake.getYPoint(0))

    def test_pickingUp_notFirstPoint(self):
        punto = Punto(self.xValue + 1, self.yValue)
        self.snake.pickingUp(punto)
        self.assertNotEqual(self.snake.body[1], self.snake.body[0])

    def test_pickingUp_growArray_return_True(self):
        punto = Punto(self.xValue + 1, self.yValue)
        self.snake.pickingUp(punto)
        self.assertTrue(2== len(self.snake.body))

    def test_pickingUp_growArray_return_False(self):
        newpunto = Punto(self.xValue + 1, self.yValue)
        self.snake.pickingUp(newpunto)
        self.assertFalse(1== len(self.snake.body))

    def test_moveRight_Snake_len(self):
        self.snake.moveRight()
        self.assertEqual(1, len(self.snake.body))

    def test_moveRight_Snake_yCoordenade(self):
        yCoordenade = self.snake.getYPoint(0)
        self.snake.moveRight()
        self.assertEqual(yCoordenade + 1, self.snake.getYPoint(0))

    def test_moveLeft_Snake_yCoordenade(self):
        yCoordenade = self.snake.getYPoint(0)
        self.snake.moveLeft()
        self.assertEqual(yCoordenade - 1, self.snake.getYPoint(0))

    def test_moveUp_Snake_xCoordenade(self):
        xCoordenade = self.snake.getXPoint(0)
        self.snake.moveUp()
        self.assertEqual(xCoordenade - 1, self.snake.getXPoint(0))

    def test_moveDown_Snake_xCoordenade(self):
        xCoordenade = self.snake.getXPoint(0)
        self.snake.moveDown()
        self.assertEqual(xCoordenade + 1, self.snake.getXPoint(0))


if __name__ == '__main__':
    unittest.main()
