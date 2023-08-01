from tkinter import Canvas, Frame
from clases import Table
import time

class Game():
   
   def __init__(self,root):
       self.key = ""
       self.table =Table()
       self.root = root
       self.tabl = Frame(self.root, width=700, height=500, background="green")
       self.tabl.pack(expand=True, fill='both')
       self.canvas = Canvas(self.tabl, width=450, height=450)
       self.canvas.place(anchor="center")
       self.canvas.pack(expand=True)
       self.draw_table()
       self.table.printTable()
       self.game() 
   def game(self):
       self.root.bind('<Key>',self.event)
       
   def event(self,event):
       self.key = event.keysym
       if self.key == "Up" and self.table.game_Over == False:
            self.table.controller("w")
            self.table.printTable()
            self.draw_table()
            print(self.table.game_Over)
       elif self.key == "Down":
            self.table.controller("s")
            self.table.printTable()
            self.draw_table()
            print("Pa rriba")
       elif self.key == "Left":
            self.table.controller("a")   
            self.table.printTable()
            self.draw_table()
            print("Pa rriba")
       elif self.key == "Right":
            self.table.controller("d")   
            self.table.printTable()
            self.draw_table()
            print("Pa rriba")
   def gameOver(self):
        self.tabl.destroy

   def draw_table(self):
        cell_width = int(450 / self.table.YLEN)
        cell_height = int(450 / self.table.XLEN)
        for y in range(self.table.XLEN):
            for x in range(self.table.YLEN):
                cell_value = self.table.table[y][x]
                color = "black"  # Por defecto, color negro (celda vacía)
                if cell_value == self.table.SNAKE:
                    color = "white"  # Color blanco para representar la serpiente
                elif cell_value == self.table.FOOD:
                    color = "red"  # Color rojo para representar la comida

                self.canvas.create_rectangle(
                    x * cell_width + 50,
                    y * cell_height + 50,
                    (x + 1) * cell_width + 50,
                    (y + 1) * cell_height + 50,
                    outline=color,
                    fill=color,
                )
     