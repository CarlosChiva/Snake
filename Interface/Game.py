from tkinter import Canvas, Frame, Tk
import tkinter
from clases import Table
import time
from scores import Scores
import threading
import view_score

class Game():
   canvas_width= 450
   canvas_height= 450
   root :tkinter
   stop_thread= False
   def __init__(self,root):
    self.root = root
    self.initial_state()
   
   def initial_state(self):
        self.key = ""
        self.last_direction = ""
        self.last_direction_lock = threading.Lock()  # Crear un objeto de bloqueo
        self.generate_moves_thread = None
        self.score = 0
        self.table = Table() 
    # main frame
        self.main_frame = Frame(self.root, bg="green")
        self.main_frame.grid(row=0, column=0, sticky="nsew")

# Configurar cómo las filas y columnas dentro de main_frame se expanden
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)    # canvas frame
        
        
        self.canvas_frame = Frame(self.main_frame, width=self.canvas_width, height=self.canvas_height, bg="green")
        self.canvas_frame.grid(row=0, column=0, sticky="nsew")
    
    # canvas
        self.canvas = Canvas(self.canvas_frame, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.grid(row=0, column=0)
    
    # sources
        self.info_frame = Frame(self.main_frame, bg="green")
        self.info_frame.grid(row=0, column=1, padx=7)
    
        self.source_label = tkinter.Label(self.info_frame, text="Current Source", font=("Arial", 16), bg="green")
        self.source_label.pack(pady=10)
    
        self.score_label = tkinter.Label(self.info_frame, text="0", font=("Arial", 16), bg="green")
        self.score_label.pack(pady=10)
        self.pause_button = tkinter.Button(self.info_frame,text="Pause",command=self.pause)
        self.pause_button.pack(pady=20)
        self.button_load=tkinter.Button(self.info_frame,text="Load Game",command=self.load_game)
        self.button_load.pack(pady=10)
        
        
        
    # Configurar las opciones de las filas y columnas para que se expandan con el cambio del tamaño de la ventana
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid_rowconfigure(0, weight=1)
        self.start_generating_moves()
        self.draw_table()
        self.root.bind('<Key>',self.event)  
        self.table.printTable()
        
   #-----------------------controller---------------------------------------------            
   def event(self,event):
          self.key = event.keysym
          self.last_direction = event
          match self.key:
            case "Up":
                self.table.controller("w")
            case "Down":
                self.table.controller("s")
            case "Left":
                self.table.controller("a")
            case "Right":
                self.table.controller("d")   
          self.table.printTable()
          self.draw_table()
          if self.table.game_Over == True:
               self.gameOver()       
# ------------------------------Thread functions--------------------------------------------------
   def generate_moves_thread_func(self):
       while self.table.game_Over == False and not self.stop_thread:
            with self.last_direction_lock:
                direction = self.last_direction
                if direction != "":
                    self.event(direction)
            time.sleep(0.7)

   def start_generating_moves(self):
        # Crear un hilo que ejecute generate_moves_thread_func()
        self.generate_moves_thread = threading.Thread(target=self.generate_moves_thread_func)
        self.generate_moves_thread.daemon = True  # Hacer que el hilo sea un hilo demonio para que se detenga cuando se cierre la aplicación
        self.generate_moves_thread.start()  # Iniciar el hilo
        
#----------------------------------Paint Table------------------------------
   def draw_table(self):
        self.score_label.config(text =str(self.table.source))
        cell_width = int(self.canvas_width / self.table.YLEN)
        cell_height = int(self.canvas_height / self.table.XLEN)
        self.canvas.delete("all")
        offset_x = (self.canvas_width - (self.table.YLEN * cell_width)) // 2
        offset_y = (self.canvas_height - (self.table.XLEN * cell_height)) // 2
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
   #---------------------------------GameOver--------------------------------------------
   def gameOver(self):
        self.root.unbind('<Key>')
        scores = Scores()
        scores.write_score(new_score=self.table.source)
        self.clear_frame()
        self.generate_window()
#----------------------------------------Window to Game over---------------------------------
   def generate_window(self):
    self.label_game_over = tkinter.Label(self.main_frame, text="Game Over", font=("Arial", 24), bg="green")
    self.label_game_over.grid(row=0, column=0, columnspan=3)
    self.label_score = tkinter.Label(self.main_frame, text="Your score:", font=("Arial", 24), bg="green")
    self.label_score.grid(row=1, column=0, columnspan=3,rowspan=1)

    self.label_value_score = tkinter.Label(self.main_frame,  font=("Arial", 18), bg="green")
    self.label_value_score.config(text= str(self.table.source))
    self.label_value_score.grid(row=2, column=0, columnspan=3,rowspan=2)
    # Frame to button
    self.button_frame = tkinter.Frame(self.main_frame, bg="green")
    self.button_frame.grid(row=5, column=0, columnspan=3)
    # Button
    button1 = tkinter.Button(self.button_frame, text="New Game", command=self.new_game)
    button1.grid(row=0, column=0, padx=10, pady=45)
    button2 = tkinter.Button(self.button_frame, text="View scores", command=self.load_scores)
    button2.grid(row=1, column=0, padx=10, pady=45)
    button3 = tkinter.Button(self.button_frame, text="Exit",command=exit)
    button3.grid(row=2, column=0, padx=10, pady=45)

    # set expansion to row and columns
    self.button_frame.grid_columnconfigure(0, weight=1)
    self.button_frame.grid_columnconfigure(1, weight=1)
    self.button_frame.grid_columnconfigure(2, weight=1)
   
   def clear_frame(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
# ------------------------------Buttons Functions----------------------------------
   def pause(self):
        self.root.unbind('<Key>')
        self.stop_thread = True
        self.pause_button.config(text="Resume",command=self.resume)
   def resume(self):
        self.pause_button.config(text="Pause",command=self.pause)
        self.root.bind('<Key>',self.event)  
        self.stop_thread = False
        self.start_generating_moves()


   def load_game(self):
       pass
   def save_game(self):
       pass
   def new_game(self):
        self.clear_frame()
        self.initial_state()

   def load_scores(self):
        self.clear_frame()
        view_score.ViewScore(self.root)
    


