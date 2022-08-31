from Punto import *


class Snake():
    body = []

    def __init__(self, punto):
        self.punto = Punto(punto.xCoordenade, punto.yCoordenade)
        self.body.append(punto)

    def pickingUp(self, xCoordenade, yCoordenade):
        weird = len(self.body) - 1
        newHead = Punto(xCoordenade, yCoordenade)
        while weird > 0:
            self.body[weird] = self.body[weird - 1]
        self.body[0].insert(0, newHead)

    def getPoint(self, index):
        self.punto = self.body[index]
        return self.punto
