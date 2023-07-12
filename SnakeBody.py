from Punto import Punto


class Snake():
    body = []

    # ------------------------------Builder-----------------------------
    def __init__(self, punto):
        if isinstance(punto,Punto):
            self.body.append(punto)
        else:
            pass   

    # ------------------------------Getters----------------------------
    def getXPoint(self, index):
       return self.body[index].getXCoordenade()

    def getYPoint(self,index):
       return self.body[index].getYCoordenade()
    # ----------------------------Feetself-----------------------------
    def pickingUp(self, newPoint):
        self.body.insert(0, newPoint)

    # ------------------------------Movements--------------------------
    def moveRight(self):
        self.body.insert(0, Punto(self.getXPoint(0), self.getYPoint(0) + 1))
        self.body.pop()

    def moveLeft(self):
        self.body.insert(0, Punto(self.getXPoint(0), self.getYPoint(0) - 1))
        self.body.pop()

    def moveUp(self):
        self.body.insert(0, Punto(self.getXPoint(0) - 1,  self.getYPoint(0)))
        self.body.pop()

    def moveDown(self):
        self.body.insert(0, Punto(self.getXPoint(0) + 1, self.getYPoint(0)))
        self.body.pop()
