from tkinter import *

root =Tk()
root.title("Simple Calculator by @mahfujarr")
img = PhotoImage(file='d:\Mahfujar.jpg')
root.iconphoto(False, img)

entry = Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# entry.pack()

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear():
    entry.delete(0, END)

def button_add():
    # entry.insert(0,"+")
    first_number = entry.get()
    global f_num
    global operation
    operation = "add"
    f_num = int(first_number)
    entry.delete(0, END)

def button_sub():
    # entry.insert(0,"+")
    first_number = entry.get()
    global f_num
    global operation
    operation = "sub"
    f_num = int(first_number)
    entry.delete(0, END)

def button_multi():
    # entry.insert(0,"+")
    first_number = entry.get()
    global f_num
    global operation
    operation = "multi"
    f_num = int(first_number)
    entry.delete(0, END)

def button_div():
    # entry.insert(0,"+")
    first_number = entry.get()
    global f_num
    global operation
    operation = "div"
    f_num = int(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    global s_num
    s_num = int(second_number)
    
    if (operation == "add"):
        entry.insert(0, f_num + s_num)
    if (operation == "sub"):
        entry.insert(0, f_num - s_num)
    if (operation == "multi"):
        entry.insert(0, f_num * s_num)
    if (operation == "div"):
        entry.insert(0, f_num / s_num)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_sub = Button(root, text="-", padx=40, pady=20, command=button_sub)
button_multi = Button(root, text="*", padx=40, pady=20, command=button_multi)
button_div = Button(root, text="/", padx=40, pady=20, command=button_div)

button_equal = Button(root, text="=", padx=87, pady=20, command=button_equal)
button_clear = Button(root, text="CLEAR", padx=25, pady=10, command=button_clear)


#Put buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_clear.grid(row=0, column=3)
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_multi.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_equal.grid(row=4, column=1, columnspan=2)



root.mainloop()