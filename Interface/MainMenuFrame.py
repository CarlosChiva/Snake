from tkinter import *


class Menu:
    def __init__(self, master):
        self.frame1 = Frame(master, width=500, height=500, background="red")
        self.frame1.pack()
        self.frame2 = Frame(self.frame1, width=100, height=100)
        secondLabel = Label(self.frame1, text="Welcome", fg="red", font=("Arial", 18))
        secondLabel.place(x=285, y=100)
        newGameButton = Button(self.frame2, text="New Game")
        newGameButton.grid(row=100, column=0, pady=20, padx=10)
        newGameButton2 = Button(self.frame2, text="Load Game")
        newGameButton2.grid(row=100, column=1, pady=20, padx=10)
        newGameButton3 = Button(self.frame2, text="View Scores")
        newGameButton3.grid(row=100, column=2, pady=20, padx=10)

        self.frame2.pack()
