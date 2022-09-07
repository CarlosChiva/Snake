from tkinter import *

root = Tk()
root.title("Menu")
root.iconbitmap("snake.ico")
root.geometry("700x500")
root.resizable(False, False)


def buildGame():
    global secondFrame, firstFrame
    secondFrame.destroy()
    firstFrame = Frame(root, width=800, height=400)
    firstFrame.pack()
    firstFrame.config(background="black", padx=10, pady=10)
    tablero = Canvas(firstFrame)
    tablero.pack(fill="both", expand=1)
    for i in range(10):
        for j in range(15):
            if (i + j) % 2 == 0:
                tablero.create_rectangle(i * 80, j * 80, (i + 1) * 80, (j + 1) - 80, fill="black")
            else:

                tablero.create_rectangle(i * 80, j * 80, (i + 1) * 80, (j + 1) - 80, fill="white")


def newGameWindows():
    secondLabel.destroy()
    newGameButton.destroy()
    newGameButton2.destroy()
    newGameButton3.destroy()
    buildGame()


firstFrame = Frame(root, width=100, height=200)
firstFrame.config(padx=100, pady=100)
firstFrame.pack()
secondFrame = Frame(root, width=100, height=200)
secondFrame.pack()
secondLabel = Label(firstFrame, text="Welcome", fg="red", font=("Arial", 18))
secondLabel.place(x=285, y=100)
secondLabel.pack()
newGameButton = Button(secondFrame, text="New Game", command=newGameWindows)
newGameButton.grid(row=1, column=0, pady=20, padx=10)
newGameButton2 = Button(secondFrame, text="Load Game")
newGameButton2.grid(row=1, column=1, pady=20, padx=10)

newGameButton3 = Button(secondFrame, text="View Scores")
newGameButton3.grid(row=1, column=2, pady=20, padx=10)

root.mainloop()
