from tkinter import *
from principal import Pincipal

root = Tk()
root.title("Snake")
#root.iconbitmap("/home/dread/VsCode/Snake/Interface/snake.ico")
root.geometry("700x500")
root.resizable(True,True)
main = Menu(root)
principal = Pincipal(root)
root.mainloop()
