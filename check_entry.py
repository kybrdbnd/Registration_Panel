from tkinter import *


class CheckEntry(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.name = StringVar(self)
        self.slip_no = StringVar(self)
        self.gui()

    def gui(self):
        Label(self, text="Enter Student's Name", font=("", 12)).grid(padx=10, pady=10)
        Entry(self, textvariable=self.name).grid(row=0, column=2, padx=10)
        Label(self, text="OR", font=("", 15)).grid()
        Label(self, text="Enter Slip no", font=("", 12)).grid(padx=10, pady=10)
        Entry(self, textvariable=self.slip_no, width=10).grid(row=2, column=2, padx=10, sticky=W)
        Button(self, text="Search", command=self.check_entry).grid(row=3,column=0,sticky=N+E)
        return

    def check_entry(self):
        print("working")
        return


if __name__ == '__main__':
    app = CheckEntry()
    app.master.title("Registration")
    app.master.geometry("+500+100")
    app.mainloop()
