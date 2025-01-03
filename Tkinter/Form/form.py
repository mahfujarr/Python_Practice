import tkinter as tk
import tkcalendar as tkc
import tkinter.messagebox as mb
import csv

class Form(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Form')
        self.geometry('300x300')

        name_frame = tk.Frame(self)
        self.label_name = tk.Label(name_frame, text='Name:')
        self.label_name.pack(side=tk.LEFT, anchor='w')
        self.name = tk.Entry(name_frame)
        self.name.pack(side=tk.LEFT, anchor='w')
        name_frame.pack(pady=5, anchor='w')

        email_frame = tk.Frame(self)
        self.label_email = tk.Label(email_frame, text='Email:')
        self.label_email.pack(side=tk.LEFT, anchor='w')
        self.email = tk.Entry(email_frame)
        self.email.pack(side=tk.LEFT, anchor='w')
        email_frame.pack(pady=5, anchor='w')
        
        phone_frame = tk.Frame(self)
        self.label_phone = tk.Label(phone_frame, text='Phone:')
        self.label_phone.pack(side=tk.LEFT, anchor='w')
        self.phone = tk.Entry(phone_frame)
        self.phone.pack(side=tk.LEFT, anchor='w')
        phone_frame.pack(pady=5, anchor='w')

        address_frame = tk.Frame(self)
        self.label_address = tk.Label(address_frame, text='Address:')
        self.label_address.pack(side=tk.LEFT, anchor='w')
        self.address = tk.Entry(address_frame)
        self.address.pack(side=tk.LEFT, anchor='w')
        address_frame.pack(pady=5, anchor='w')

        gender_frame = tk.Frame(self)
        self.label_gender = tk.Label(gender_frame, text='Gender:')
        self.label_gender.pack(side=tk.LEFT, anchor='w')
        self.gender_var = tk.StringVar(value='Male')
        self.radio_male = tk.Radiobutton(gender_frame, text='Male', variable=self.gender_var, value='Male')
        self.radio_female = tk.Radiobutton(gender_frame, text='Female', variable=self.gender_var, value='Female')
        self.radio_nonBinary = tk.Radiobutton(gender_frame, text='Non-binary', variable=self.gender_var, value='Non-Binary')
        self.radio_male.pack(side=tk.LEFT, anchor='w')
        self.radio_female.pack(side=tk.LEFT, anchor='w')
        self.radio_nonBinary.pack(side=tk.LEFT, anchor='w')
        gender_frame.pack(pady=5, anchor='w')

        dob_frame = tk.Frame(self)
        self.label_dob = tk.Label(dob_frame, text='Date of Birth:')
        self.label_dob.pack(side=tk.LEFT, anchor='w')
        self.dob = tkc.DateEntry(dob_frame, datepattern='dd-mm-yyyy')
        self.dob.set_date('01-01-2000')
        self.dob.pack(side=tk.LEFT, anchor='w')
        dob_frame.pack(pady=5, anchor='w')

        self.button = tk.Button(self, text='Submit', command=self.on_submit)
        self.button.pack()

        self.button.bind("<Enter>", self.on_hover)
        self.button.bind("<Button-1>", self.on_click)
        self.button.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        self.button.config(bg='green', fg='white')

    def on_click(self, event):
        self.button.config(bg='green', fg='red')

    def on_leave(self, event):
        self.button.config(bg='SystemButtonFace', fg='black')


    def on_submit(self):
        name = self.name.get()
        email = self.email.get()
        phone = self.phone.get()
        address = self.address.get()
        gender = self.gender_var.get()
        dob = self.dob.get_date()
        
        with open('form_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, phone, address, gender, dob])
        mb.showinfo("Success", "Form submitted successfully!")
        self.name.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.gender_var.set('Male')
        self.dob.set_date('01-01-2000')

if __name__ == '__main__':
    form = Form()
    form.mainloop()