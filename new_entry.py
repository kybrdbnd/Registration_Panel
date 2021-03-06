import sqlite3
from tkinter import messagebox
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


class NewEntry(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.slip_no = StringVar(self)
        self.name = StringVar(self)
        self.branch = StringVar(self)
        self.section = StringVar(self)
        self.email_id = StringVar(self)
        self.phone_no = StringVar(self)
        self.shirt_size = StringVar(self)
        self.gui()

    def gui(self):
        Label(self, text="Slip No:", font=("", 12)).grid(row=0, sticky=E, ipadx=20, ipady=10)
        Entry(self, textvariable=self.slip_no).grid(row=0, column=1)
        Label(self, text="Name:", font=("", 12)).grid(row=1, sticky=E, ipadx=20, ipady=10)
        Entry(self, textvariable=self.name).grid(row=1, column=1)
        Label(self, text="Branch", font=("", 12)).grid(row=2, sticky=E, ipadx=20, ipady=10)
        Entry(self, textvariable=self.branch).grid(row=2, column=1)
        Label(self, text="Section:", font=("", 12)).grid(row=3, sticky=E, ipadx=20, ipady=10)
        Entry(self, textvariable=self.section).grid(row=3, column=1)
        Label(self, text="Phone No:", font=("", 12)).grid(row=4, sticky=E, ipadx=20, ipady=10)
        Entry(self, textvariable=self.phone_no).grid(row=4, column=1)
        Label(self, text="Email ID:", font=("", 12)).grid(row=5, sticky=E, ipadx=20, ipady=10)
        Entry(self, textvariable=self.email_id).grid(row=5, column=1)
        Label(self, text="Shirt Size:", font=("", 12)).grid(row=6, sticky=E, ipadx=20, ipady=10)
        self.shirt_size.set("S")
        choices = ["S", "M", "L", "XL"]
        OptionMenu(self, self.shirt_size, *choices).grid(row=6, column=1, sticky=W)
        Button(self, text="OK", command=self.make_entry, width=10).grid(row=7, columnspan=2, ipadx=20)
        return

    def make_entry(self):
        values = (self.slip_no.get(), self.name.get().upper(), self.branch.get().upper(), self.section.get().upper(),
                  self.phone_no.get().upper(), self.email_id.get().upper(), self.shirt_size.get())
        if self.slip_no.get().isdigit():
            if len(self.slip_no.get()) == 0:
                messagebox.showerror("Registration", message="Please enter Slip No.")
            else:
                if len(self.name.get()) == 0:
                    messagebox.showerror("Registration", message="Please enter student name")
                else:
                    try:
                        c.execute('insert into new_entries values (?,?,?,?,?,?,?)', values)
                        conn.commit()
                        Label(self, text="Successfully entered").grid(row=7, column=2)
                    except:
                        messagebox.showerror("Registration", message="Slip no. already enrolled")
                        conn.rollback()
        else:
            messagebox.showerror("Registration", message="Enter a valid Slip No.")
        return


if __name__ == '__main__':
    myapp = NewEntry()
    myapp.master.title("Make Entry")
    myapp.master.geometry("500x350+500+100")
    myapp.mainloop()
