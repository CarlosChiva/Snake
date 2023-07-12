import random

from SnakeBody import Snake
from Punto import Punto


class Table():
    XLEN = 15
    YLEN = 10
    table = [[]]
    EMPTY = 0
    FOOD = 2
    SNAKE = 1
    source = 0
    game_Over = False
       # -----------------------------------------Builder--------------------------------------------
    def __init__(self):
        self.table = [[self.EMPTY for i in range(self.YLEN)] for i in range(self.XLEN)]
        self.__generaTeTable()
        print("Creado el tablero")
        self.__putSnake()
        self.__foodGenerator()

    def __generaTeTable(self):
        for i in range(self.XLEN):
            for j in range(self.YLEN):
                if self.table[i][j] != self.FOOD:
                    self.table[i][j] = self.EMPTY

    def __putSnake(self):
        newPoint = Punto(self.__randomXNumber(), self.__randomYNumber())
        self.snakeBody = Snake(newPoint)
        print("creada la serpiente")
        self.__putValues()
        print("Insertada la serpiente")

    # -------------------------------------Put snake---------------------------------------------
    def __putValues(self):
        self.__generaTeTable()
        count = 0
        while count < len(self.snakeBody.body):
            self.table[self.snakeBody.body[count].getXCoordenade()][
                self.snakeBody.body[count].getYCoordenade()] = self.SNAKE
            count += 1

    # ---------------------------------------Food generator--
    def __foodGenerator(self):
        x = self.__randomXNumber()
        y = self.__randomYNumber()

        if self.table[x][y] == self.EMPTY:
            self.table[x][y] = self.FOOD

        else:
            self.__foodGenerator()
        print("Food generate ")

    def snakeXCord(self):
        return self.snakeBody.getXPoint()

    def snakeYCord(self):
        return self.snakeBody.getYPoint()

    def __sumScore(self):
        self.source += 100
    # --------------------------------------Booleans---------------------------------------------

    def __checkThereAreSnake(self, xCoordenade, yCoordenade):
        return self.table[xCoordenade][yCoordenade] != self.SNAKE

    def __checkThereIsFood(self, xCoordenade, yCoordenade):
        return self.table[xCoordenade][yCoordenade] == self.FOOD

    def __canUp(self):
        checkX = self.snakeBody.getXPoint(0) - 1
        checkY = self.snakeBody.getYPoint(0)
        return checkX >= 0 and self.__checkThereAreSnake(checkX, checkY)

    def __canDown(self):
        checkX = self.snakeBody.getXPoint(0) + 1
        checkY = self.snakeBody.getYPoint(0)
        return checkX  <= self.XLEN - 1 and self.__checkThereAreSnake(checkX, checkY)

    def __canLeft(self):
         checkX = self.snakeBody.getXPoint(0)
         checkY = self.snakeBody.getYPoint(0) - 1
         return checkY >= 0 and self.__checkThereAreSnake(checkX, checkY)

    def __canRight(self):
        checkX = self.snakeBody.getXPoint(0)
        checkY = self.snakeBody.getYPoint(0) + 1
        return checkY <= self.YLEN - 1 and self.__checkThereAreSnake(checkX, checkY)

    # -------------------------------Random Number generater-------------------
    def __randomXNumber(self):
        return random.randrange(0, self.XLEN)

    def __randomYNumber(self):
        return random.randrange(0, self.YLEN)

    # ----------------------------------Snake actions-------------------------------------------
    def __moveSnakeRight(self):
        if self.__checkThereIsFood(self.snakeBody.getXPoint(0), self.snakeBody.getYPoint(0) + 1):
            self.snakeBody.pickingUp(Punto(self.snakeBody.getXPoint(0), self.snakeBody.getYPoint(0) + 1))
            self.__sumScore()
            self.__foodGenerator()
        else:
            self.snakeBody.moveRight()
        self.__putValues()

    def __moveSnakeLeft(self):
        if self.__checkThereIsFood(self.snakeBody.getXPoint(0), self.snakeBody.getYPoint(0) - 1):
            self.snakeBody.pickingUp(Punto(self.snakeBody.getXPoint(0), self.snakeBody.getYPoint(0) - 1))
            self.__sumScore()
            self.__foodGenerator()
        else:
            self.snakeBody.moveLeft()
        self.__putValues()

    def __moveSnakeUp(self):
        if self.__checkThereIsFood(self.snakeBody.getXPoint(0) - 1, self.snakeBody.getYPoint(0)):
            self.snakeBody.pickingUp(Punto(self.snakeBody.getXPoint(0) - 1, self.snakeBody.getYPoint(0)))
            self.__sumScore()
            self.__foodGenerator()
        else:
            self.snakeBody.moveUp()
        self.__putValues()

    def __moveSnakeDown(self):
        if self.__checkThereIsFood(self.snakeBody.getXPoint(0) + 1, self.snakeBody.getYPoint(0)):
            self.snakeBody.pickingUp(Punto(self.snakeBody.getXPoint(0) + 1, self.snakeBody.getYPoint(0)))
            self.__sumScore()
            self.__foodGenerator()
        else:
            self.snakeBody.moveDown()
        self.__putValues()


    # -------------------------------------Controller--------------------------------------------
    def controller(self, direction):
        if direction == "w" and self.__canUp():
            self.__moveSnakeUp()
        elif direction == 's' and self.__canDown():
            self.__moveSnakeDown()
        elif direction == 'a' and self.__canLeft():
            self.__moveSnakeLeft()
        elif direction == 'd' and self.__canRight():
            self.__moveSnakeRight()
        else:
            self.gameOver()

    # ---------------------------------------------Game Over--------------------------------------
    def gameOver(self):
        self.game_Over = True
        print("Game Over")
        print("Your source: " + str(self.source))


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
