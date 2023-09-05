import random

from ..clases import Punto
from ..clases import Snake

class Table():
    XLEN = 15
    YLEN = 10
    table = [[]]
    EMPTY = 0
    FOOD = 2
    SNAKE = 1
    source = 0
    game_Over = False
    snakeBody = Snake
    def __init__(self, snake):
        self.table = [[self.EMPTY for i in range(self.YLEN)] for i in range(self.XLEN)]
        self.__generaTeTable()
        print("Creado el tablero")
        self.snakeBody= snake
        self.putSnake(self.snakeBody)
        self.__foodGenerator()

    def __generaTeTable(self):
        for i in range(self.XLEN):
            for j in range(self.YLEN):
                if self.table[i][j] != self.FOOD:
                    self.table[i][j] = self.EMPTY

    def putSnake(self, snake):
        self.snakeBody = snake
        print("creada la serpiente")
        self.__putValues()
        print("Insertada la serpiente")

    def __putValues(self):
        count = 0
        while count < len(self.snakeBody.body):
            self.table[
                self.snakeBody.body[count].getXCoordenade()][
                self.snakeBody.body[count].getYCoordenade()] = self.SNAKE
            count += 1

    def sumScore(self):
        self.source += 100
        self.__foodGenerator()


    # --------------------------------------Booleans---------------------------------------------

    def checkThereAreSnake(self, xCoordenade, yCoordenade):
        return self.table[xCoordenade][yCoordenade] == self.SNAKE

    def checkThereIsFood(self, xCoordenade, yCoordenade):
        return self.table[xCoordenade][yCoordenade] == self.FOOD

    def canUp(self):
        checkX = self.snakeBody.getXPoint(0) - 1
        checkY = self.snakeBody.getYPoint(0)
        return checkX >= 0 and not self.checkThereAreSnake(checkX, checkY)

    def canDown(self):
        checkX = self.snakeBody.getXPoint(0) + 1
        checkY = self.snakeBody.getYPoint(0)
        return checkX <= self.XLEN - 1 and not self.checkThereAreSnake(checkX, checkY)

    def canLeft(self):
        checkX = self.snakeBody.getXPoint(0)
        checkY = self.snakeBody.getYPoint(0) - 1
        return checkY >= 0 and not self.checkThereAreSnake(checkX, checkY)

    def canRight(self):
        checkX = self.snakeBody.getXPoint(0)
        checkY = self.snakeBody.getYPoint(0) + 1
        return checkY <= self.YLEN - 1 and not self.checkThereAreSnake(checkX, checkY)

    # -------------------------------Random Number generater-------------------
    def __randomXNumber(self):
        return random.randrange(0, self.XLEN)

    def __randomYNumber(self):
        return random.randrange(0, self.YLEN)

    # ----------------------------------Snake actions-------------------------------------------

    def moveSnakeRight(self):
        if self.checkThereIsFood(self.snakeBody.getXPoint(0), self.snakeBody.getYPoint(0) + 1):
            self.snakeBody.pickingUp(Punto(self.snakeBody.getXPoint(0), self.snakeBody.getYPoint(0) + 1))
            self.sumScore()
        else:
            self.snakeBody.moveRight()
        self.__putValues()

    def moveSnakeLeft(self):
        if self.checkThereIsFood(self.snakeBody.getXPoint(0), self.snakeBody.getYPoint(0) - 1):
            self.snakeBody.pickingUp(Punto(self.snakeBody.getXPoint(0), self.snakeBody.getYPoint(0) - 1))
            self.sumScore()
        else:
            self.snakeBody.moveLeft()
        self.__putValues()

    def moveSnakeUp(self):
        if self.checkThereIsFood(self.snakeBody.getXPoint(0) - 1, self.snakeBody.getYPoint(0)):
            self.snakeBody.pickingUp(Punto(self.snakeBody.getXPoint(0) - 1, self.snakeBody.getYPoint(0)))
            self.sumScore()
        else:
            self.snakeBody.moveUp()
        self.__putValues()

    def moveSnakeDown(self):
        if self.checkThereIsFood(self.snakeBody.getXPoint(0) + 1, self.snakeBody.getYPoint(0)):
            self.snakeBody.pickingUp(Punto(self.snakeBody.getXPoint(0) + 1, self.snakeBody.getYPoint(0)))
            self.sumScore()
        else:
            self.snakeBody.moveDown()
        self.__putValues()

 
    # -------------------------------------Controller--------------------------------------------
    def controller(self, direction):
        if direction == "w" and self.canUp():
            self.moveSnakeUp()
        elif direction == 's' and self.canDown():
            self.moveSnakeDown()
        elif direction == 'a' and self.canLeft():
            self.moveSnakeLeft()
        elif direction == 'd' and self.canRight():
            self.moveSnakeRight()
        else:
            self.gameOver()

    # ---------------------------------------------Game Over--------------------------------------
    def gameOver(self):
        self.game_Over = True
        print("Game Over")
        print("Your source: " + str(self.source))

    # -----------------------------------------Builder--------------------------------------------



    """def __init__(self):
        self.table = [[self.EMPTY for i in range(self.YLEN)] for i in range(self.XLEN)]
        print("Creado el tablero")
        self.__putSnake()
        self.__foodGenerator()
"""


    # ---------------------------------------Food generator--
    """def __foodGenerator(self):
        x = self.__randomXNumber()
        y = self.__randomYNumber()

        if self.table[x][y] == self.EMPTY:
            self.table[x][y] = self.FOOD

        else:
            self.__foodGenerator()
        print("Food generate ")
"""

    # -----------------------------------------------------------------------------------------Change
    def __foodGenerator(self):
        xCoordenade = self.__randomXNumber()
        yCoordenade = self.__randomYNumber()
        if self.table[xCoordenade][yCoordenade] == self.EMPTY:
            self.puntoFood = Punto(xCoordenade, yCoordenade)
            self.table[xCoordenade][yCoordenade] = self.FOOD

        else:
            self.__foodGenerator()
        print("Food generate ")

    # ------------------------------------Personal Printer--------------------------------
    def printTable(self):
        for i in range(self.XLEN):
            row = ""
            for j in range(self.YLEN):
                row += str(self.table[i][j]) + "   "
            print(row)
        """ 
  for r in range(self.XLEN):
            print(self.table[r])
            
         print('\n'.join([''.join(['{:3}'.format(item) for item in row])
                          for row in self.table]))
 """
