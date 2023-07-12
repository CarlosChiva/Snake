from tkinter import *
from Table import Table

def buildGame():
        table = Table()
        frame1.destroy()
        frame2.destroy()
        table = Frame(root, width=700, height=500, background="green")
        table.pack(expand=True, fill='both')
        canvas = Canvas(table, width=400, height=400, bg="black")
        canvas.pack(expand=True)
        # Dibujar el recuadro del juego
        canvas.create_rectangle(50, 50, 350, 350, outline="white")
root = Tk()
root.title("Snake")
#root.iconbitmap("/home/dread/VsCode/Snake/Interface/snake.ico")
root.geometry("700x500")
root.resizable(False, False)
main = Menu(root)
frame1 = Frame(root, width=700, height=500, background="white")
frame2 = Frame(frame1, width=100, height=100)
secondLabel = Label(frame1, text="Welcome", fg="red", font=("Arial", 18))
secondLabel.place(x=285, y=100)
newGameButton = Button(frame2, text="New Game",command=buildGame)
newGameButton.grid(row=100, column=0, pady=20, padx=10)
newGameButton2 = Button(frame2, text="Load Game")
newGameButton2.grid(row=100, column=1, pady=20, padx=10)
newGameButton3 = Button(frame2, text="View Scores")
newGameButton3.grid(row=100, column=2, pady=20, padx=10)
frame1.pack()
frame2.pack()
root.mainloop()

