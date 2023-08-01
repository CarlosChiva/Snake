from tkinter import Canvas, Frame, Tk
import tkinter
from clases import Table
import time

class Game():
   
   def __init__(self,root):
        self.key = ""
        self.score = 0
        self.table = Table()
        self.root = root
        self.main_frame = Frame(self.root,bg="green")
        self.main_frame.pack(expand=True, fill='both')

        self.canvas_frame = Frame(self.main_frame, bg="green")
        self.canvas_frame.pack(side=tkinter.LEFT, expand=True, fill='both')

        self.tabl = Frame(self.canvas_frame, bg="green")
        self.tabl.pack(expand=True, fill='both')
        
        self.canvas = Canvas(self.tabl, width=450, height=450, bg="green")
        self.canvas.pack(expand=True)
        
        self.info_frame = Frame(self.main_frame,bg="green")
        self.info_frame.pack(side=tkinter.LEFT, padx=10)
        
        self.source_label = tkinter.Label(self.info_frame, text="Current Source", font=("Arial", 16),bg="green")
        self.source_label.pack(pady=10)
        
        self.score_label = tkinter.Label(self.info_frame, text="0", font=("Arial", 16),bg="green")
        self.score_label.pack(pady=10)
        self.draw_table()
        self.table.printTable()
        self.game() 
   def game(self):
       self.root.bind('<Key>',self.event)
       
   def event(self,event):
          self.key = event.keysym
          if self.key == "Up":
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
          if self.table.game_Over == True:
               self.gameOver()       
   def gameOver(self):
        self.canvas.destroy()
        self.generate_window()

   def draw_table(self):
        self.score_label.config(text =str(self.table.source))
        cell_width = int(450 / self.table.YLEN)
        cell_height = int(450 / self.table.XLEN)
        self.canvas.delete("all")
        canvas_width = self.canvas.winfo_width()  # Get the current canvas width
        canvas_height = self.canvas.winfo_height()  # Get the current canvas height
        offset_x = (canvas_width - (self.table.YLEN * cell_width)) // 2
        offset_y = (canvas_height - (self.table.XLEN * cell_height)) // 2
        for y in range(self.table.XLEN):
            for x in range(self.table.YLEN):
                cell_value = self.table.table[y][x]
                color = "black"  # Por defecto, color negro (celda vacía)
                if cell_value == self.table.SNAKE:
                    color = "white"  # Color blanco para representar la serpiente
                elif cell_value == self.table.FOOD:
                    color = "red"  # Color rojo para representar la comida
                    self.canvas.create_oval(
                        x * cell_width + offset_x + cell_width // 4,
                        y * cell_height + offset_y + cell_height // 4,
                        (x + 1) * cell_width + offset_x - cell_width // 4,
                        (y + 1) * cell_height + offset_y - cell_height // 4,
                        outline="red",
                        fill="red",
                        width=0
                    )
                # Change rectangles to squares (use same coordinates for width and height)
                self.canvas.create_rectangle(
                    x * cell_width + offset_x,
                    y * cell_height + offset_y,
                    (x + 1) * cell_width + offset_x,
                    (y + 1) * cell_height + offset_y,
                    outline=color,
                    fill=color,
                    width=0  # Set the outline width to 0 to remove the border
                )
   def generate_window(self):
              # Label para el título de "Game Over"
     self.label_game_over = tkinter.Label(self.tabl, text="Game Over", font=("Arial", 24),bg="green")
     self.label_game_over.pack(pady=20)

    # Frame para los botones
     self.button_frame = tkinter.Frame(self.tabl,bg="green")
     self.button_frame.pack(pady=25)

    # Botones
     button1 = tkinter.Button(self.button_frame, text="New Game",command=self.new_game)
     button1.pack(pady=45)

     button2 = tkinter.Button(self.button_frame, text="View scores")
     button2.pack(pady=45)

     button3 = tkinter.Button(self.button_frame, text="Exit")
     button3.pack(pady=45)                   
   def new_game(self):
       self.label_game_over.destroy()
       self.button_frame.destroy()
       self.tabl.destroy()
       self.__init__(self.root)  