import sqlite3
from tkinter import *

conn = sqlite3.connect("registration.db")
c = conn.cursor()
try:
    c.execute('''create table new_entries(
    slip_no integer Primary Key,
    name text not null,
    branch text not null,
    section text,
    email_id text,
    phone_no integer,
    shirt_size text)''')
except:
    pass

slip_no = StringVar
name = StringVar
branch = StringVar
section = StringVar
email_id = StringVar
phone_no = StringVar
shirt_size = StringVar


class NewEntry(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()

    def gui(self):
        Label(self, text="Slip No:", font=("", 12)).grid(row=0, sticky=E, ipadx=20, ipady=10)
        Entry(self, textvariable=slip_no).grid(row=0, column=1)
        Label(self, text="Name:", font=("", 12)).grid(row=1, sticky=E, ipadx=20, ipady=10)
        Entry(self, textvariable=name).grid(row=1, column=1)
        Label(self, text="Branch", font=("", 12)).grid(row=2, sticky=E, ipadx=20, ipady=10)
        Entry(self, textvariable=branch).grid(row=2, column=1)
        Label(self, text="Section:", font=("", 12)).grid(row=3, sticky=E, ipadx=20, ipady=10)
        Entry(self, textvariable=section).grid(row=3, column=1)
        Label(self, text="Phone No:", font=("", 12)).grid(row=4, sticky=E, ipadx=20, ipady=10)
        Entry(self, textvariable=phone_no).grid(row=4, column=1)
        Label(self, text="Shirt Size:", font=("", 12)).grid(row=5, sticky=E, ipadx=20, ipady=10)
        shirt = StringVar(self)
        shirt.set("S")
        choices = ["S", "M", "L", "XL"]
        OptionMenu(self, shirt, *choices).grid(row=5, column=1, sticky=W)
        Button(self, text="OK", command=self.make_entry, width=10).grid(row=6, columnspan=2,ipadx=20)
        return

    def make_entry(self):
        print("working")
        return


myapp = NewEntry()
myapp.master.title("Make Entry")
myapp.master.geometry("500x350+500+100")

myapp.gui()

myapp.mainloop()
