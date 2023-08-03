from tkinter import Canvas, Frame, Tk
import tkinter
from scores import Scores

class ViewScore():
    def __init__(self,root):
        self.root = root 
        etiqueta_titulo = tkinter.Label(self.root, text="Puntajes de la Partida", font=("Helvetica", 16, "bold"))
        etiqueta_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        lista_scores = tkinter.Listbox(self.root, font=("Helvetica", 12), width=30)
        lista_scores.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        lista_scores.config(justify=tkinter.CENTER)
        self.score = Scores()
        for score in self.score.scores:
            lista_scores.insert(tkinter.END, score)
        # Expandir filas y columnas para centrar los elementos
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Agregar botones en las esquinas inferiores
        boton_izquierda = tkinter.Button(self.root, text="New Game")
        boton_izquierda.grid(row=2, column=0, padx=10, pady=5, sticky=tkinter.S+tkinter.W)

        boton_derecha = tkinter.Button(self.root, text="Exit",command=exit)
        boton_derecha.grid(row=2, column=1, padx=10, pady=5, sticky=tkinter.S+tkinter.E)
    