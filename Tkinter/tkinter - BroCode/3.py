from tkinter import *

count = 0
def click():
    global count
    count +=1
    displaycount.config(text=f"{count} times")

def on_enter(event):
    button['text'] = 'Nigga!'
    global count
    count +=1
    displaycount.config(text=f"{count} times")
def on_leave(event):
    button['text'] = 'You have said the N word!!'

window = Tk()
window.title('Nigga Counter')
window.geometry('800x300')
displaycount = Label(window, text=count)
displaycount.config(font=('Arial',60,'bold'))
displaycount.pack()

button = Button(text='Click me!!',font=('Arial',40,'bold'))
button.pack()
button.config(command=click)
button.config(background='black',
              fg = 'White',
              activebackground='Red')
button.bind('<Enter>', on_enter)
button.bind('<Leave>', on_leave)
window.mainloop()