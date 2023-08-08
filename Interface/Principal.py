from tkinter import *
from Game import Game
from view_score import ViewScore

def buildGame():
        frame1.destroy()
        frame2.destroy()
        game = Game(root)     
def build_view_score():
        frame1.destroy()
        frame2.destroy()
        view_score = ViewScore(root)                        

root = Tk()
root.title("Snake")
#root.iconbitmap("/home/dread/VsCode/Snake/Interface/snake.ico")
root.geometry("700x500")
root.resizable(True,True)
main = Menu(root)
frame1 = Frame(root, width=700, height=500, background="white")
frame2 = Frame(frame1, width=100, height=100)
secondLabel = Label(frame1, text="Welcome", fg="red", font=("Arial", 18))
secondLabel.place(x=285, y=100)
newGameButton = Button(frame2, text="New Game",command=buildGame)
newGameButton.grid(row=100, column=0, pady=20, padx=10)
newGameButton2 = Button(frame2, text="Load Game")
newGameButton2.grid(row=100, column=1, pady=20, padx=10)
newGameButton3 = Button(frame2, text="View Scores",command=build_view_score)
newGameButton3.grid(row=100, column=2, pady=20, padx=10)
frame1.pack()
frame2.pack()
root.mainloop()
