import sqlite3
import time
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect("registration.db")
c = conn.cursor()


class CheckEntry(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.name = StringVar(self)
        self.slip_no = StringVar(self)
        self.gui()

    def gui(self):
        Label(self, text="Enter Student's Name", font=("", 12)).grid(padx=10, pady=10)
        Entry(self, textvariable=self.name).grid(row=0, column=1, padx=10)
        Label(self, text="OR", font=("", 15)).grid()
        Label(self, text="Enter Slip no", font=("", 12)).grid(padx=10, pady=10)
        Entry(self, textvariable=self.slip_no, width=10).grid(row=2, column=1, padx=10, sticky=W)
        Button(self, text="Search", command=self.check_entry).grid(row=3, column=0, sticky=N + E)
        Label(self, text="Slip no", font=("", 12)).grid(row=4, sticky=W, padx=10, pady=10)
        Label(self, text="Name", font=("", 12)).grid(row=5, sticky=W, padx=10, pady=10)
        Label(self, text="Branch", font=("", 12)).grid(row=6, sticky=W, padx=10, pady=10)
        Label(self, text="Section", font=("", 12)).grid(row=7, sticky=W, padx=10, pady=10)
        Label(self, text="Email ID", font=("", 12)).grid(row=8, sticky=W, padx=10, pady=10)
        Label(self, text="Phone no", font=("", 12)).grid(row=9, sticky=W, padx=10, pady=10)
        Label(self, text="Shirt Size", font=("", 12)).grid(row=10, sticky=W, padx=10, pady=10)
        return

    def check_entry(self):
        if len(self.name.get()) == 0 and len(self.slip_no.get()) == 0:
            print("both missing")
            messagebox.showwarning(title="Registration", message="Please enter atleast one value")
        elif len(self.slip_no.get()) == 0:
            print("slip no missing")
            value = (self.name.get().upper(),)
            c.execute('select * from new_entries where name = ?', value)
            if len(c.fetchall()) == 0:
                messagebox.showerror(title="Registration", message="Desired entry doesn't found")
            else:
                self.name_search()
                self.name.set("")
        else:
            print("name missing")
            value = (self.slip_no.get().upper(),)
            c.execute('select * from new_entries where slip_no = ?', value)
            if len(c.fetchall()) == 0:
                messagebox.showerror(title="Registration", message="Desired entry doesn't found")
            else:
                self.slip_no_search()
                self.slip_no.set("")
        return

    def name_search(self):
        value = (self.name.get().upper(),)
        c.execute('select * from new_entries where name = ?', value)
        start_column = 0
        for columns, rows in enumerate(c.fetchall()):
            start_row = 4
            start_column += 1
            for values in rows:
                temp = StringVar(value="%s" % values)
                x = Label(self, textvariable=temp, font=("", 12))
                x.grid(row=start_row, column=start_column)
                start_row += 1
        return

    def slip_no_search(self):
        value = (self.slip_no.get().upper(),)
        c.execute('select * from new_entries where slip_no = ?', value)
        start_column = 0
        for columns, rows in enumerate(c.fetchall()):
            start_row = 4
            start_column += 1
            for values in rows:
                temp = StringVar(value="%s" % values)
                x = Label(self, textvariable=temp, font=("", 12))
                x.grid(row=start_row, column=start_column)
                start_row += 1
        return


if __name__ == '__main__':
    app = CheckEntry()
    app.master.title("Registration")
    app.master.geometry("+500+100")
    app.mainloop()
