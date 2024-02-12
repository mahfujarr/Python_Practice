from tkinter import *

root = Tk()
def onClick():
    myText = Label(root, text="Mahfujar Rahman")
    myText.pack()

myButton = Button(root, text="Click me!", command=onClick)

myButton.pack()
root.mainloop()