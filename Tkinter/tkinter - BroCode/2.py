from tkinter import *

window = Tk()
photo = PhotoImage(file='me.png')
label = Label(window,
              text='Hello!!',
              font=('Arial',40,'bold'),
              fg='Green',
              bg='Black',
              relief=RAISED,
              bd=10,
              image = photo,
              compound='top',
              padx=10,
              pady=10)
label.pack()

window.mainloop()