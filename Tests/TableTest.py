import unittest

from Punto import Punto
from TableCheck import Table
from SnakeBody import Snake


class MyTestCase(unittest.TestCase):
    puntoSnake = Punto(7, 7)
    POINTNW = Punto(0, 0)
    POINTSE = Punto(14, 9)

    def setUp(self):
        snake = Snake(self.puntoSnake)
        self.table = Table(snake)
        self.pointFood = self.table.puntoFood

    # --------------------------------- len to table
    def test_len_X(self):
        self.assertEqual(15, self.table.XLEN)  # add assertion here

    def test_len_Y(self):
        self.assertEqual(10, self.table.YLEN)  # add assertion here

    # --------------------------------- Check of the first Colocations
    def test_isThereSnake(self):
        self.assertIsNotNone(self.table.SNAKE, self.table.table)

    def test_isThereFood(self):
        self.assertIsNotNone(self.table.FOOD, self.table.table)

    # --------------------------------Movements of the Snake
    def test_Can_Move_Up_returnFalse(self):
        self.table.snakeBody.pickingUp(self.POINTNW)
        self.assertFalse(self.table.canUp())

    def test_Can_Move_Up_Snake_returnFalse(self):
        downtOfSnake = Punto(8, 7)
        self.table.snakeBody.pickingUp(downtOfSnake)
        self.assertFalse(self.table.canUp())

    def test_Can_Move_Up_returnTrue(self):
        self.table.snakeBody.pickingUp(self.POINTSE)
        self.assertTrue(self.table.canUp())

    def test_Can_Move_Down_returnTrue(self):
        self.table.snakeBody.pickingUp(self.POINTNW)
        self.assertTrue(self.table.canDown())

    def test_Can_Move_Down_returnFalse(self):
        self.table.snakeBody.pickingUp(self.POINTSE)
        self.assertFalse(self.table.canDown())

    def test_Can_Move_Down_Snake_returnFalse(self):
        upOfSnake = Punto(6, 7)
        self.table.snakeBody.pickingUp(upOfSnake)
        self.assertFalse(self.table.canDown())

    def test_Can_Move_Left_returnTrue(self):
        self.table.snakeBody.pickingUp(self.POINTSE)
        self.assertTrue(self.table.canLeft())

    def test_Can_Move_Left_returnFalse(self):
        self.table.snakeBody.pickingUp(self.POINTNW)

        self.assertFalse(self.table.canLeft())

    def test_Can_Move_Left_Snake_returnFalse(self):
        rightOfSnake = Punto(7, 8)
        self.table.snakeBody.pickingUp(rightOfSnake)
        self.assertFalse(self.table.canLeft())

    def test_Can_Move_right_returnTrue(self):
        self.table.snakeBody.pickingUp(self.POINTNW)
        self.assertTrue(self.table.canRight())

    def test_Can_Move_right_returnFalse(self):
        self.table.snakeBody.pickingUp(self.POINTSE)
        self.assertFalse(self.table.canRight())

    def test_Can_Move_right_Snake_returnFalse(self):
        leftOfSnake = Punto(7, 6)
        self.table.snakeBody.pickingUp(leftOfSnake)
        self.assertFalse(self.table.canRight())

    # -----------------------------------------EAT FOOD
    def test_moveUpSnake_Food(self):
        expected = self.table.source + 100
        down_of_Food = Punto(self.table.puntoFood.getXCoordenade() + 1, self.table.puntoFood.getYCoordenade())
        self.table.snakeBody.pickingUp(down_of_Food)
        self.table.moveSnakeUp()
        self.assertTrue(self.table.source == expected)

    def test_moveDownSnake_Food(self):
        expected = self.table.source + 100
        up_of_Food = Punto(self.table.puntoFood.getXCoordenade() - 1, self.table.puntoFood.getYCoordenade())
        self.table.snakeBody.pickingUp(up_of_Food)
        self.table.moveSnakeDown()
        self.assertTrue(self.table.source == expected)

    def test_moveLeftSnake_Food(self):
        expected = self.table.source + 100
        right_of_Food = Punto(self.table.puntoFood.getXCoordenade(), self.table.puntoFood.getYCoordenade() + 1)
        self.table.snakeBody.pickingUp(right_of_Food)
        self.table.moveSnakeLeft()
        self.assertTrue(self.table.source == expected)

    def test_moveRightSnake_Food(self):
        expected = self.table.source + 100
        left_of_Food = Punto(self.table.puntoFood.getXCoordenade(), self.table.puntoFood.getYCoordenade() - 1)
        self.table.snakeBody.pickingUp(left_of_Food)
        self.table.moveSnakeRight()
        self.assertTrue(self.table.source == expected)

    # ----------------------------------------------Movement
    def test_moveRightSnake(self):
        expected = Punto(self.table.snakeBody.getXPoint(), self.table.snakeBody.getYPoint() + 1)
        self.table.moveSnakeRight()
        actual = Punto(self.table.snakeBody.getXPoint(), self.table.snakeBody.getYPoint())
        self.assertTrue(
            expected.getXCoordenade() == actual.getXCoordenade() and expected.getYCoordenade() == actual.getYCoordenade())

    def test_moveLeftSnake(self):
        expected = Punto(self.table.snakeBody.getXPoint(), self.table.snakeBody.getYPoint() - 1)
        self.table.moveSnakeLeft()
        actual = Punto(self.table.snakeBody.getXPoint(), self.table.snakeBody.getYPoint())
        self.assertTrue(
            expected.getXCoordenade() == actual.getXCoordenade() and expected.getYCoordenade() == actual.getYCoordenade())
    def test_moveUpSnake(self):
        expected = Punto(self.table.snakeBody.getXPoint()-1, self.table.snakeBody.getYPoint())
        self.table.moveSnakeUp()
        actual = Punto(self.table.snakeBody.getXPoint(), self.table.snakeBody.getYPoint())
        self.assertTrue(expected.getXCoordenade() == actual.getXCoordenade() and expected.getYCoordenade() == actual.getYCoordenade())
    def test_moveDownSnake(self):
        expected = Punto(self.table.snakeBody.getXPoint()+1, self.table.snakeBody.getYPoint())
        self.table.moveSnakeDown()
        actual = Punto(self.table.snakeBody.getXPoint(), self.table.snakeBody.getYPoint())
        self.assertTrue(
            expected.getXCoordenade() == actual.getXCoordenade() and expected.getYCoordenade() == actual.getYCoordenade())


if __name__ == '__main__':
    unittest.main()
