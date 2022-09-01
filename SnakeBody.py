from Punto import *


class Snake():
    body = []

    # ------------------------------Builder-----------------------------
    def __init__(self, punto):
        self.body.append(punto)

    # ------------------------------Getters----------------------------
    def getXPoint(self):
        return self.body[0].getXCoordenade()

    def getYPoint(self):
        return self.body[0].getYCoordenade()

    # ----------------------------Feetself-----------------------------
    def pickingUp(self, newPoint):
        self.body.insert(0, newPoint)

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
