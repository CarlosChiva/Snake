from tkinter import *
from MainMenuFrame import *
root = Tk()
root.title("Snake")
root.iconbitmap("snake.ico")
root.geometry("700x500")
root.resizable(False, False)
main = Menu(root)
root.mainloop()
"""def buildGame():
    global secondFrame, firstFrame
    secondFrame.destroy()
    firstFrame = Frame(root, width=800, height=400, background="black", padx=10, pady=10)
    firstFrame.place(x=10, rely=10, relwidth=.25, relheight=.25)
    firstFrame.pack()
    tablero = Canvas(firstFrame)
    tablero.pack(expand=True)
    for i in range(10):
        for j in range(15):
            if (i + j) % 2 == 0:
                tablero.create_rectangle(i * 30, j * 30, (i + 1) * 30, (j + 1) - 30, fill="black")
            else:

                tablero.create_rectangle(i * 30, j * 30, (i + 1) * 30, (j + 1) - 30, fill="white")
"""
