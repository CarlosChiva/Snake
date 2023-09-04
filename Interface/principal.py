from tkinter import *

class Principal():
        def __init__(self,root,change_window):
                self.root = root
                self.function = change_window
                self.frame1 = Frame(self.root, width=700, height=500, background="white")
                self.frame2 = Frame(self.frame1, width=100, height=100)
                self.secondLabel = Label(self.frame1, text="Welcome", fg="red", font=("Arial", 18))
                self.secondLabel.place(x=285, y=100)
                self.newGameButton = Button(self.frame2, text="New Game",command=self.buildGame)
                self.newGameButton.grid(row=100, column=0, pady=20, padx=10)
                self.newGameButton2 = Button(self.frame2, text="Load Game",command=self.build_load_game)
                self.newGameButton2.grid(row=100, column=1, pady=20, padx=10)
                self.newGameButton3 = Button(self.frame2, text="View Scores",command=self.build_view_score)
                self.newGameButton3.grid(row=100, column=2, pady=20, padx=10)
                self.frame1.pack()
                self.frame2.pack()
        def destroy_main_frames(self):
                self.frame1.destroy()
                self.frame2.destroy()
        def buildGame(self):
                self.destroy_main_frames()
                self.function("game")     
        def build_view_score(self):
                self.destroy_main_frames()
                self.function("score")
        def build_load_game(self):
                self.destroy_main_frames()
                self.function("load_game")