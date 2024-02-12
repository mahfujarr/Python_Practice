from tkinter import *
root =Tk()

entry = Entry(root, width=50)
entry.pack()

def onClick():
    hello = f"Hello {entry.get()}"
    label = Label(root, text=hello)
    label.pack()

button = Button(root, text= "Ok", command=onClick)
button.pack()

root.mainloop()