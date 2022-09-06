from tkinter import *

root = Tk()
root.title("Menu")
# root.iconbitmap()
firstFrame = Frame(root, width=700, height=500)
firstFrame.pack()
secondLabel = Label(firstFrame, text="Welcome", fg="red", font=("Arial", 18))
secondLabel.place(x=285, y=200)

root.mainloop()
