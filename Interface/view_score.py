from tkinter import Canvas, Frame, Tk
import tkinter
import Game
from scores import Scores

class ViewScore():
    def __init__(self,root):
        self.root = root 
        self.etiqueta_titulo = tkinter.Label(self.root, text="Puntajes de la Partida", font=("Helvetica", 16, "bold"))
        self.etiqueta_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        self.lista_scores = tkinter.Listbox(self.root, font=("Helvetica", 12), width=30)
        self.lista_scores.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        self.lista_scores.config(justify=tkinter.CENTER)
        self.score = Scores()
        for date, score in self.score.scores.items():
            date_str = date.strftime("%Y-%m-%d %H:%M:%S")
            self.lista_scores.insert(tkinter.END, f"{date_str} - Score: {score}")
        # Expandir filas y columnas para centrar los elementos
     

        # Agregar botones en las esquinas inferiores
        self.boton_izquierda = tkinter.Button(self.root, text="New Game",command=self.newGame)
        self.boton_izquierda.grid(row=2, column=0, padx=10, pady=5, sticky=tkinter.S+tkinter.W)

        self.boton_derecha = tkinter.Button(self.root, text="Exit",command=exit)
        self.boton_derecha.grid(row=2, column=1, padx=10, pady=5, sticky=tkinter.S+tkinter.E)
    def newGame(self):
        self.etiqueta_titulo.destroy()
        self.lista_scores.destroy()
        self.boton_izquierda.destroy()
        self.boton_derecha.destroy()
        game = Game.Game(self.root)