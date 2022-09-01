from Punto import *


class Snake():
    body = []

    # ------------------------------Builder-----------------------------
    def __init__(self, punto):
        self.puntx = Punto(punto.xCoordenade, punto.yCoordenade)
        self.body.append(self.puntx)

    # ------------------------------Getters----------------------------
    def getXPoint(self, index):
        return self.body[index].getXCoordenade()

    def getYPoint(self, index):
        return self.body[index].getYCoordenade()

    # ----------------------------Feetself-----------------------------
    def pickingUp(self, xCoordenade, yCoordenade):
        weird = len(self.body) - 1
        newHead = Punto(xCoordenade, yCoordenade)
        while weird > 0:
            self.body[weird] = self.body[weird - 1]
        self.body[0].insert(0, newHead)

    # ------------------------------Movements--------------------------
    def moveRight(self):
        self.body.insert(0, Punto(self.body[0].getXCoordenade(), self.body[0].getYCoordenade() + 1))
        self.body.pop()

    def moveLeft(self):
        self.body.insert(0, Punto(self.body[0].getXCoordenade(), self.body[0].getYCoordenade() - 1))
        self.body.pop()

    def moveUp(self):
        self.body.insert(0, Punto(self.body[0].getXCoordenade() - 1, self.body[0].getYCoordenade()))
        self.body.pop()

    def moveDown(self):
        self.body.insert(0, Punto(self.body[0].getXCoordenade() + 1, self.body[0].getYCoordenade()))
        self.body.pop()
    # --------------------------Snake Queue---------------------------
