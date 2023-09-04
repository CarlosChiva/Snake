from tkinter import *
from windows_provider import Windows_provider
root = Tk()
root.title("Snake")
#root.iconbitmap("/home/dread/VsCode/Snake/Interface/snake.ico")
root.geometry("700x500")
root.resizable(True,True)
main = Menu(root)
window = Windows_provider(root)
root.mainloop()
