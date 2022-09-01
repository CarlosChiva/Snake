import random

from SnakeBody import Snake
from Punto import *


class Table():
    XLEN = 15
    YLEN = 10
    table = [[]]
    EMPTY = 0
    FOOD = 2
    SNAKE = 1

    # --------------------------------------Booleans---------------------------------------------
    def __canUp(self):
        return self.snakeBody.getXPoint() > 0 and self.table[self.snakeBody.getXPoint() - 1][
            self.snakeBody.getYPoint()] != self.SNAKE

    def __canDown(self):
        return self.snakeBody.getXPoint() < self.XLEN - 1 and self.table[self.snakeBody.getXPoint() + 1][
            self.snakeBody.getYPoint()] != self.SNAKE

    def __canLeft(self):
        return self.snakeBody.getYPoint() > 0 and self.table[self.snakeBody.getXPoint()][
            self.snakeBody.getYPoint() - 1] != self.SNAKE

    def __canRight(self):
        return self.snakeBody.getYPoint() < self.YLEN - 1 and self.table[self.snakeBody.getXPoint()][
            self.snakeBody.getYPoint() + 1] != self.SNAKE

    # -------------------------------Random Number generater-------------------
    def __randomXNumber(self):
        return random.randrange(0, self.XLEN)

    def __randomYNumber(self):
        return random.randrange(0, self.YLEN)

    # ----------------------------------Snake actions-------------------------------------------
    def __moveSnakeRight(self):
        if self.table[self.snakeBody.getXPoint()][self.snakeBody.getYPoint() + 1] == self.FOOD:
            self.snakeBody.pickingUp(Punto(self.snakeBody.getXPoint(), self.snakeBody.getYPoint() + 1))
            self.__foodGenerator()
        else:
            self.snakeBody.moveRight()
        self.__putValues()

    def __moveSnakeLeft(self):
        if self.table[self.snakeBody.getXPoint()][self.snakeBody.getYPoint() - 1] == self.FOOD:
            self.snakeBody.pickingUp(Punto(self.snakeBody.getXPoint(), self.snakeBody.getYPoint() - 1))
            self.__foodGenerator()
        else:
            self.snakeBody.moveLeft()
        self.__putValues()

    def __moveSnakeUp(self):
        if self.table[self.snakeBody.getXPoint() - 1][self.snakeBody.getYPoint()] == self.FOOD:
            self.snakeBody.pickingUp(Punto(self.snakeBody.getXPoint() - 1, self.snakeBody.getYPoint()))
            self.__foodGenerator()
        else:
            self.snakeBody.moveUp()
        self.__putValues()

    def __moveSnakeDown(self):
        if self.table[self.snakeBody.getXPoint() + 1][self.snakeBody.getYPoint()] == self.FOOD:
            self.snakeBody.pickingUp(Punto(self.snakeBody.getXPoint() + 1, self.snakeBody.getYPoint()))
            self.__foodGenerator()
        else:
            self.snakeBody.moveDown()
        self.__putValues()

    # -------------------------------------Put snake---------------------------------------------
    def __putValues(self):
        self.__generaTeTable()
        count = 0
        while count < len(self.snakeBody.body):
            self.table[self.snakeBody.body[count].getXCoordenade()][
                self.snakeBody.body[count].getYCoordenade()] = self.SNAKE
            count += 1

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
            print("Error")

    # -----------------------------------------Builder--------------------------------------------
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
