import os
from tkinter import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

    def gui(self):
        Label(self, text="Registration Panel", font=("", 20)).pack(pady=15)
        Button(self, text="New Entry", font=("", 10), command=self.new_entry).pack(pady=30)
        Button(self, text="Check Entry", font=("", 10), command=self.check_entry).pack(pady=30)
        Button(self, text="Make Excel file", font=("", 10), command=self.convert_db).pack(pady=30)

    def new_entry(self):
        os.system("py -3 new_entry.py")
        return

    def check_entry(self):
        print("working")
        return

    def convert_db(self):
        print("working")
        return

        # create the application


myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("Registration Panel")
myapp.master.geometry("500x350+500+100")
myapp.gui()


# start the program
myapp.mainloop()
