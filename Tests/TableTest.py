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

    def tearDown(self):
        self.table.snakeBody.body.clear()

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
        expected = Punto(self.table.snakeBody.getXPoint() - 1, self.table.snakeBody.getYPoint())
        self.table.moveSnakeUp()
        actual = Punto(self.table.snakeBody.getXPoint(), self.table.snakeBody.getYPoint())
        self.assertTrue(
            expected.getXCoordenade() == actual.getXCoordenade() and expected.getYCoordenade() == actual.getYCoordenade())

    def test_moveDownSnake(self):
        expected = Punto(self.table.snakeBody.getXPoint() + 1, self.table.snakeBody.getYPoint())
        self.table.moveSnakeDown()
        actual = Punto(self.table.snakeBody.getXPoint(), self.table.snakeBody.getYPoint())
        self.assertTrue(
            expected.getXCoordenade() == actual.getXCoordenade() and expected.getYCoordenade() == actual.getYCoordenade())

    # -----------------------------Checkers Food and Snake------------------------------
    def test_CheckAreThereSnake_returnTrue(self):
        x = self.table.snakeXCord()
        y = self.table.snakeYCord()
        self.assertTrue(self.table.checkThereAreSnake(x, y))

    def test_CheckAreThereSnake_returnFalse(self):
        x = self.table.snakeXCord() - 1
        y = self.table.snakeYCord() + 1
        self.assertFalse(self.table.checkThereAreSnake(x, y))

    def test_CheckIsThereFood_returnFalse(self):
        x = self.table.snakeBody.getXPoint()
        y = self.table.snakeBody.getYPoint()
        self.assertFalse(self.table.checkThereIsFood(x, y))

    def test_CheckIsThereFood_returnTrue(self):
        x = self.table.puntoFood.getXCoordenade()
        y = self.table.puntoFood.getYCoordenade()
        self.assertTrue(self.table.checkThereIsFood(x, y))

    def test_sumScore(self):
        n = self.table.source
        self.table.sumScore()
        self.assertTrue(n + 100 == self.table.source)

    def test_snakeXCord(self):
        self.assertTrue(self.table.snakeXCord() == self.table.snakeBody.getXPoint())

    def test_snakeYCord(self):
        self.assertTrue(self.table.snakeYCord() == self.table.snakeBody.getYPoint())

    # -------------------------------Game Over----------------------
    def test_gameover_returnFalse(self):
        self.assertFalse(self.table.game_Over)

    def test_gameover_returnTrue_OutOfTable_Left(self):
        self.table.snakeBody.pickingUp(self.POINTNW)
        self.table.controller('a')
        self.assertTrue(self.table.game_Over)

    def test_gameover_returnTrue_OutOfTable_Up(self):
        self.table.snakeBody.pickingUp(self.POINTNW)
        self.table.controller('w')
        self.assertTrue(self.table.game_Over)

    def test_gameover_returnTrue_OutOfTable_right(self):
        self.table.snakeBody.pickingUp(self.POINTSE)
        self.table.controller('d')
        self.assertTrue(self.table.game_Over)

    def test_gameover_returnTrue_OutOfTable_down(self):
        self.table.snakeBody.pickingUp(self.POINTSE)
        self.table.controller('s')
        self.assertTrue(self.table.game_Over)

    def test_gameOver_returnTrue_Snake_left(self):
        self.table.snakeBody.pickingUp(Punto(self.table.snakeXCord(), self.table.snakeYCord() + 1))
        self.table.controller('a')
        self.assertTrue(self.table.game_Over)

    def test_gameOver_returnTrue_Snake_right(self):
        self.table.snakeBody.pickingUp(Punto(self.table.snakeXCord(), self.table.snakeYCord() - 1))
        self.table.controller('d')
        self.assertTrue(self.table.game_Over)

    def test_gameOver_returnTrue_Snake_up(self):
        self.table.snakeBody.pickingUp(Punto(self.table.snakeXCord()+1, self.table.snakeYCord() ))
        self.table.controller('w')
        self.assertTrue(self.table.game_Over)

    def test_gameOver_returnTrue_Snake_down(self):
        self.table.snakeBody.pickingUp(Punto(self.table.snakeXCord()-1, self.table.snakeYCord()))
        self.table.controller('s')
        self.assertTrue(self.table.game_Over)


if __name__ == '__main__':
    unittest.main()
