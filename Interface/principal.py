from tkinter import *

class Principal():
        def __init__(self,root,change_window):
                self.root = root
                self.function = change_window
                self.root.grid_rowconfigure(0, weight=1)
                self.root.grid_columnconfigure(0, weight=1)
                # main frame
                self.main_frame = Frame(self.root, bg="green")
                self.main_frame.grid(row=0, column=0, sticky="nsew")
                # Configurar cómo las filas y columnas dentro de main_frame se expanden
             
                
                self.secondLabel = Label(self.main_frame, text="Welcome",background="green", fg="red", font=("Arial", 18))
                
                self.secondLabel.grid(row=0, column=1,pady=50)
                
                self.newGameButton = Button(self.main_frame, text="New Game",command=self.buildGame)
                self.newGameButton.grid(row=1, column=0,pady=50,padx=70)
                self.newGameButton2 = Button(self.main_frame, text="Load Game",command=self.build_load_game)
                self.newGameButton2.grid(row=1, column=1,padx=70)
                self.newGameButton3 = Button(self.main_frame, text="View Scores",command=self.build_view_score)
                self.newGameButton3.grid(row=1, column=2,padx=70)

        def destroy_main_frames(self):
                self.main_frame.destroy()
        
        def buildGame(self):
                self.destroy_main_frames()
                self.function("game")     
        def build_view_score(self):
                self.destroy_main_frames()
                self.function("score")
        def build_load_game(self):
                self.destroy_main_frames()
                self.function("load_game")