import random

from SnakeBody import Snake
from Punto import *


class Table():
    XLEN = int(15)
    YLEN = int(10)
    table = [[]]
    EMPTY = int(0)
    FOOD = int(2)
    SNAKE = int(1)

    # --------------------------------------Booleans---------------------------------------------
    def canUp(self):
        return self.snakeBody.getXPoint(0) > 0

    def canDown(self):
        return self.snakeBody.getXPoint(0) < self.XLEN - 1

    def canLeft(self):
        return self.snakeBody.getYPoint(0) > 0

    def canRight(self):
        return self.snakeBody.getYPoint(0) < self.YLEN - 1

    # -------------------------------Random Number generater-------------------
    def __randomXNumber(self):
        return random.randrange(0, self.XLEN)

    def __randomYNumber(self):
        return random.randrange(0, self.YLEN)

    # ----------------------------------Snake actions-------------------------------------------
    def moveSnakeRight(self):
        self.snakeBody.moveRight()
        self.putValues()

    def moveSnakeLeft(self):
        self.snakeBody.moveLeft()
        self.putValues()

    def moveSnakeUp(self):
        self.snakeBody.moveUp()
        self.putValues()

    def moveSnakeDown(self):
        self.snakeBody.moveDown()
        self.putValues()

    # -------------------------------------Put snake---------------------------------------------
    def putValues(self):
        self.generaTeTable()
        count = 0
        while count < len(self.snakeBody.body):
            self.table[self.snakeBody.getXPoint(count)][self.snakeBody.getYPoint(count)] = self.SNAKE
            count += 1

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
            print("Error")

    # -----------------------------------------Builder--------------------------------------------
    def generaTeTable(self):
        for i in range(self.XLEN):
            for j in range(self.YLEN):
                if self.table[i][j] != self.FOOD:
                    self.table[i][j] = self.EMPTY

    def __putSnake(self):
        newPoint = Punto(self.__randomXNumber(), self.__randomYNumber())
        self.snakeBody = Snake(newPoint)
        print("creada la serpiente")
        self.putValues()
        print("Insertada la serpiente")

    def __init__(self):
        self.table = [[self.EMPTY for i in range(self.YLEN)] for i in range(self.XLEN)]
        print("Creado el tablero")
        self.__putSnake()
        self.__foodGenerator()

    # ---------------------------------------Food generator--
    def __foodGenerator(self):
        x = self.__randomXNumber()
        y = self.__randomYNumber()

        if self.table[x][y] == self.EMPTY:
            self.table[x][y] = self.FOOD

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
