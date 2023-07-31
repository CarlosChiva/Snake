from tkinter import Canvas, Frame
from clases import Table


class Game():
   
   def __init__(self,root):
       self.key = ""
       self.table =Table()
       self.root = root
       tabl = Frame(self.root, width=700, height=500, background="green")
       tabl.pack(expand=True, fill='both')
       self.canvas = Canvas(tabl, width=400, height=400, bg="black")
       self.canvas.pack(expand=True)
       self.table.draw_table(self.canvas)
       self.table.printTable()
       self.game() 
   def game(self):
       self.root.bind('<Key>',self.event)
       self.root.mainloop()
           
   def event(self,event):
       self.key = event.keysym
       if self.key == "Up":
            self.table.controller("w")
            self.table.printTable()
            self.table.draw_table(self.canvas)
            print("Pa rriba")
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