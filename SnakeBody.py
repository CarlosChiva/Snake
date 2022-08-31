from Punto import *


class Snake():
    body = []

    def __init__(self, punto):
        self.puntx = Punto(punto.xCoordenade, punto.yCoordenade)
        self.body.append(self.puntx)

    def pickingUp(self, xCoordenade, yCoordenade):
        weird = len(self.body) - 1
        newHead = Punto(xCoordenade, yCoordenade)
        while weird > 0:
            self.body[weird] = self.body[weird - 1]
        self.body[0].insert(0, newHead)

    def getXPoint(self, index):
        self.puntx = self.body[index]
        return self.puntx.getXCoordenade()

    def getYPoint(self, index):
        self.puntx = self.body[index]
        return self.puntx.getYCoordenade()


