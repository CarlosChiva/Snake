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
    # main frame
        self.main_frame = Frame(self.root, bg="green")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
    
    # canvas frame
        self.canvas_frame = Frame(self.main_frame, bg="green")
        self.canvas_frame.grid(row=0, column=0, sticky="nsew")
    
    # canvas
        self.canvas = Canvas(self.canvas_frame, width=450, height=450, bg="green")
        self.canvas.grid(row=0, column=0, sticky="nsew")
    
    # sources
        self.info_frame = Frame(self.main_frame, bg="green")
        self.info_frame.grid(row=0, column=1, padx=10, sticky="nsew")
    
        self.source_label = tkinter.Label(self.info_frame, text="Current Source", font=("Arial", 16), bg="green")
        self.source_label.pack(pady=10)
    
        self.score_label = tkinter.Label(self.info_frame, text="0", font=("Arial", 16), bg="green")
        self.score_label.pack(pady=10)

    # Configurar las opciones de las filas y columnas para que se expandan con el cambio del tamaño de la ventana
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid_rowconfigure(0, weight=1)
        self.start_game()
        self.root.bind('<Key>',self.event)  

   def start_game(self):
        self.draw_table()
        self.table.printTable()
        self.draw_table()
               
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
          elif self.key == "Left":
               self.table.controller("a")   
               self.table.printTable()
               self.draw_table()
          elif self.key == "Right":
               self.table.controller("d")   
               self.table.printTable()
               self.draw_table()
          if self.table.game_Over == True:
               self.gameOver()       

   def gameOver(self):
        self.root.unbind('<Key>')
     # Eliminar todos los componentes en el canvas
        self.canvas.destroy()
    # Eliminar todos los componentes en el info_frame
        for widget in self.info_frame.winfo_children():
          widget.destroy()
    # Destruir los frames principales
        self.canvas_frame.destroy()
        self.info_frame.destroy()
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
     
    self.label_game_over = tkinter.Label(self.main_frame, text="Game Over", font=("Arial", 24), bg="green")
    self.label_game_over.pack(pady=20)
    self.label_game_over.grid(row=0, column=0, columnspan=3)

    # Frame para los botones
    self.button_frame = tkinter.Frame(self.main_frame, bg="green")
    self.button_frame.grid(row=1, column=0, columnspan=3)

    # Botones
    button1 = tkinter.Button(self.button_frame, text="New Game", command=self.new_game)
    button1.grid(row=0, column=0, padx=10, pady=45)

    button2 = tkinter.Button(self.button_frame, text="View scores")
    button2.grid(row=1, column=0, padx=10, pady=45)

    button3 = tkinter.Button(self.button_frame, text="Exit")
    button3.grid(row=2, column=0, padx=10, pady=45)

    # Configurar opciones de expansión para filas y columnas
    self.root.grid_rowconfigure(0, weight=1)
    self.root.grid_rowconfigure(1, weight=1)
    self.root.grid_columnconfigure(0, weight=1)
    self.button_frame.grid_columnconfigure(0, weight=1)
    self.button_frame.grid_columnconfigure(1, weight=1)
    self.button_frame.grid_columnconfigure(2, weight=1)

   def new_game(self):
       self.label_game_over.destroy()
           # Eliminar los botones
       for widget in self.button_frame.winfo_children():
        widget.destroy()
    # Destruir el marco de botones
       self.button_frame.destroy()
       self.__init__(self.root)
