import random

class Punto():


    def __init__(self, xCoordenade, yCoordenade):
        self.xCoordenade = xCoordenade
        self.yCoordenade = yCoordenade

    def getXCoordenade(self):
        return self.xCoordenade

    def getYCoordenade(self):
        return self.yCoordenade

    def setXCoordenade(self, newXCoordenade):
        self.xCoordenade = newXCoordenade

    def setYCoordenade(self, newYCoordenade):
        self.yCoordenade = newYCoordenade



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


class Table():
    XLEN = 15
    YLEN = 10
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

    def draw_table(self, canvas):
        cell_width = int(300 / self.YLEN)
        cell_height = int(300 / self.XLEN)
        for y in range(15):
            for x in range(10):
                cell_value = self.table[y][x]
                color = "black"  # Por defecto, color negro (celda vacía)
                if cell_value == self.SNAKE:
                    color = "white"  # Color blanco para representar la serpiente
                elif cell_value == self.FOOD:
                    color = "red"  # Color rojo para representar la comida

                canvas.create_rectangle(
                    x * cell_width + 50,
                    y * cell_height + 50,
                    (x + 1) * cell_width + 50,
                    (y + 1) * cell_height + 50,
                    outline=color,
                    fill=color,
                )

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
    # --------------------------------------getter---------------------------------------------
    def getTable(self):
        return self.table
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
