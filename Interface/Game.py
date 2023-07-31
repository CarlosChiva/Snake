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
       self.canvas = Canvas(self.tabl, width=350, height=350, bg="black")
       self.canvas.place(anchor="nw")
       self.canvas.pack(expand=True)
       self.table.draw_table(self.canvas)
       self.table.printTable()
       self.game() 
   def game(self):
       self.root.bind('<Key>',self.event)
       
   def event(self,event):
       self.key = event.keysym
       if self.key == "Up" and self.table.game_Over == False:
            self.table.controller("w")
            self.table.printTable()
            self.table.draw_table(self.canvas)
            print(self.table.game_Over)
       elif self.key == "Down":
            self.table.controller("s")
            self.table.printTable()
            self.table.draw_table(self.canvas)
            print("Pa rriba")
       elif self.key == "Left":
            self.table.controller("a")   
            self.table.printTable()
            self.table.draw_table(self.canvas)
            print("Pa rriba")
       elif self.key == "Right":
            self.table.controller("d")   
            self.table.printTable()
            self.table.draw_table(self.canvas)
            print("Pa rriba")
   def gameOver(self):
        self.tabl.destroy