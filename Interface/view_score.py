from tkinter import Canvas, Frame, Tk
import tkinter
from .scores import Scores

class ViewScore():
    def __init__(self,root,change_window):
        self.root = root 
        self.function= change_window
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        # main frame
        self.main_frame = Frame(self.root, bg="green")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        # Configurar cómo las filas y columnas dentro de main_frame se expanden
        self.main_frame.grid_rowconfigure(0, weight=0)  # No necesitamos que la primera fila dentro de main_frame expanda
        self.main_frame.grid_rowconfigure(1, weight=1)  # Queremos que la segunda fila dentro de main_frame expanda
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        
        self.etiqueta_titulo = tkinter.Label(self.main_frame, text="Scores", font=("Helvetica", 16, "bold"),bg="green")
        self.etiqueta_titulo.grid(row=0, column=0, columnspan=2, pady=5,sticky="n")
        self.lista_scores = tkinter.Listbox(self.main_frame, font=("Helvetica", 12), width=30)
        self.lista_scores.grid(row=1, column=0, columnspan=2, padx=10, pady=100,sticky="n")
        self.lista_scores.config(justify=tkinter.CENTER)
  
        self.score = Scores()
        index = 0
        for date, score in self.score.get_scores().items():
            index += 1
            date_str = date.strftime("%m-%d %H:%M:%S")
            if index <=10:
                self.lista_scores.insert(tkinter.END, f"{date_str} - Score: {score}")
            else:
                break

        # Agregar botones en las esquinas inferiores
        self.boton_izquierda = tkinter.Button(self.main_frame, text="New Game",command=self.newGame)
        self.boton_izquierda.grid(row=2, column=0, padx=10, pady=5, sticky=tkinter.S+tkinter.W)

        self.boton_derecha = tkinter.Button(self.main_frame, text="Exit",command=exit)
        self.boton_derecha.grid(row=2, column=1, padx=10, pady=5, sticky=tkinter.S+tkinter.E)
    def newGame(self):
        self.etiqueta_titulo.destroy()
        self.lista_scores.destroy()
        self.boton_izquierda.destroy()
        self.boton_derecha.destroy()
        self.function("game")