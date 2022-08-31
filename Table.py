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

    # ----------------------------------------Snake actions--------------------------------------
    def putValues(self):
        count = 0

        while count < len(self.snakeBody.body):
           puntoAunx=self.snakeBody.getPoint(count)

    def __putSnake(self):
        newPoint = Punto(self.__randomXNumber(), self.__randomYNumber())
        self.snakeBody = Snake(newPoint)
        self.putValues()

    # -------------------------------------Builder----------------------------------------
    def __init__(self):
        self.table = [[0 for i in range(self.YLEN)] for i in range(self.XLEN)]
        self.__putSnake()

    # ------------------------------------Personal Printer--------------------------------
    def printTable(self):
        print('\n'.join([''.join(['{:3}'.format(item) for item in row])
                         for row in self.table]))
