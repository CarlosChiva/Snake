import random

from SnakeBody import Snake
from Punto import *


class Table():
    XLEN = 20
    YLEN = 15
    table = [[]]

    # ----------------------------------------Random Number generater----------------------------
    def __randomXNumber(self):
        return random.randrange(0, self.XLEN)

    def __randomYNumber(self):
        return random.randrange(0, self.YLEN)

    # ---------------------------------------Food generator--------------------------------------
    def __foodGenerator(self):
        x = self.__randomXNumber()
        y = self.__randomYNumber()

        if self.table[y][x] == 0:
            self.table[y][x] = 2

        else:
            self.__foodGenerator()
        print("Food generate ")

    # ----------------------------------------Snake actions--------------------------------------

    def putValues(self):
        count = 0

        while count < len(self.snakeBody.body):
            self.table[self.snakeBody.getXPoint(count)][self.snakeBody.getYPoint(count)] = 1
            count += 1

    print("Insertada la serpiente")

    def __putSnake(self):
        newPoint = Punto(self.__randomXNumber(), self.__randomYNumber())
        self.snakeBody = Snake(newPoint)
        print("creada la serpiente")
        self.putValues()

    # -------------------------------------Builder----------------------------------------
    def __init__(self):
        self.table = [[0 for i in range(self.YLEN)] for i in range(self.XLEN)]
        print("Creado el tablero")
        self.__putSnake()
        self.__foodGenerator()

    # ------------------------------------Personal Printer--------------------------------
    def printTable(self):
        print('\n'.join([''.join(['{:3}'.format(item) for item in row])
                         for row in self.table]))
